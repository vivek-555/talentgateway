from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import *
from django.contrib.auth.decorators import login_required
from decorators import group_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from django.views.decorators.http import require_http_methods
import json
from tasks import *
from celery.result import AsyncResult
import time
from django.conf import settings
from forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.http import Http404
from django.views import generic

AWS_ACCESS_KEY_ID = settings.AWS_SETTINGS["access_key_id"]
AWS_SECRET_ACCESS_KEY = settings.AWS_SETTINGS["secret_access_key"]
AWS_BUCKET_NAME = settings.AWS_SETTINGS["bucket_name"]


class JobListView(generic.ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'job_listing.html'
    paginate_by = 10


@require_http_methods(["GET"])
def job_detail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        form = JobApplicantForm()
    except Exception as e:
        raise Http404("Job does not exist")
    return render(request, "job_detail.html", {"job": job, "form": form})


@require_http_methods(["POST"])
def job_apply(request):
    files = request.FILES
    form = JobApplicantForm(request.POST)
    if form.is_valid() and files:
        file_name = files["resume"].name

        s3_utils.upload_to_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, files["resume"], AWS_BUCKET_NAME,
                              file_name)

        job_applicant = form.save()
        job_applicant.resume_url = file_name
        job_id = request.POST.get("job_id")
        job_applicant.job.add(Job.objects.get(id=int(job_id)))

        job_applicant.save()
        messages.add_message(request, messages.SUCCESS, 'Applied successfully!')
        return redirect("/")
    else:
        pass


@login_required(login_url='/accounts/login/')
def homepage(request, *args, **kwargs):
    return render(request, "home.html")


def job_listing(request, *args, **kwargs):
    return render(request, "job_listing.html")


@login_required(login_url='/accounts/login/')
def get_task_status(request, task_id):
    res = AsyncResult(task_id)
    state = res.state
    return JsonResponse({"state": state})


@login_required(login_url='/accounts/login/')
@csrf_exempt
def updload_records(request):
    if request.method == "GET":
        return render(request, "updload_records.html")
    if request.method == "POST":
        files = request.FILES
        excel_file = files["excel_file"]
        rar_file = files["rar_file"]

        excel_file_name = save_temp_file(excel_file, "excel")
        rar_file_name = save_temp_file(rar_file, "rar")

        batch_id = get_random_string(length=7)

        task = parse_file.delay(excel_file_name, rar_file_name, batch_id)
        task_id = task.task_id

        return JsonResponse({
            "status": True,
            "message": "Processing",
            "data": {
                "task_id": str(task_id),
                "batch_id": batch_id
            }
        })


FILE_EXT_MAP = {
    "excel": ".xlsx",
    "rar": ".rar",
    "doc": ".doc",
    "docx": ".docx",
    "pdf": ".pdf"
}


def save_temp_file(file_obj, file_type):
    file_ext = FILE_EXT_MAP[file_type]
    file_name = str(int(time.time())) + file_ext
    with open(settings.BASE_DIR + '/temp/' + file_type + '/' + file_name, 'w+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return file_name


@login_required(login_url='/accounts/login/')
@require_http_methods(["GET"])
def download(request, path):
    # deprecated for now
    path = path.strip('/')
    url = s3_utils.get_s3_url(aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY, file_name=path, bucket=AWS_BUCKET_NAME)

    return HttpResponse(url)


@login_required(login_url='/accounts/login/')
# @group_required(group_names=["data-entry operator"], redirect_url='/unauthorized/')
def user_list_page(request):
    global_filters = Filter.objects.all().filter(type="Global")
    local_filters = request.user.filter_set.all()
    degrees = Degree.objects.all().filter(~Q(name__icontains="any"))
    skills = Skill.objects.all()
    batch_ids = set(Customer.objects.values_list('batch_id', flat=True))
    location = STATE_CHOICES
    context = {
        "count": len(global_filters) + len(local_filters),
        "global_filters": global_filters,
        "local_filters": local_filters,
        "degrees": degrees,
        "skills": skills,
        "location": location,
        "batch_ids": batch_ids,
    }

    return render(request, 'customer_list.html', context)


@require_http_methods(["GET"])
def get_filters(request):
    global_filters = Filter.objects.all().filter(type="Global")
    local_filters = request.user.filter_set.all()
    filters = {
        "count": len(global_filters) + len(local_filters),
        "global_filters": global_filters,
        "local_filters": local_filters
    }

    return render(request, '_filter_list.html', filters)


@require_http_methods(["POST"])
def save_filter(request):
    response = {
        "status": False,
        "data": None,
        "message": None
    }
    post_data = request.POST
    filter_name = post_data.get("filter_name", None)
    filter_data = post_data.get("filter_data", None)

    if not filter_data or not filter_name:
        return JsonResponse(response)

    existing_filter = Filter.objects.all().filter(name=filter_name, created_by=request.user.email)
    if existing_filter:
        response["message"] = "Filter name must be unique"
        return JsonResponse(response)

    filter_obj = Filter(name=filter_name, data=json.loads(filter_data),
                        created_by=request.user.email, type="Local")
    filter_obj.save()
    filter_obj.user.add(request.user)

    return JsonResponse(response)


@login_required(login_url='/accounts/login/')
@group_required(group_names=["data-entry operator"], redirect_url='/unauthorized/')
@require_http_methods(["GET"])
def edit_record(request, id):
    _id = int(id.split('-')[1])
    user = Customer.objects.get(id=_id)

    url = None

    # check if the user has resume
    if user.resume_url:
        path = user.resume_url.strip('/')
        url = s3_utils.get_s3_url(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, file_name=path, bucket=AWS_BUCKET_NAME)

    form = UserForm(instance=user, initial={
        'primary_skills': user.primary_skills.split(",") if user.primary_skills else None,
        'secondary_skills': user.secondary_skills.split(",") if user.secondary_skills else None,
    })

    return render(request, "edit_customer.html", {"user": user, "form": form, "url": url})


@login_required(login_url='/accounts/login/')
@group_required(group_names=["data-entry operator"], redirect_url='/unauthorized/')
@require_http_methods(["POST"])
def save_record(request):
    user = Customer.objects.get(id=int(request.POST.get("user_id")))
    form = UserForm(request.POST, instance=user)

    try:

        update_degrees(form=form, request=request)
        update_college(form=form, request=request)
        update_company(form=form, request=request)
        update_skill(form=form, request=request)
        update_course(form=form, request=request)
        update_industry(form=form, request=request)
        update_functional_area(form=form, request=request)

        form.save()
    except Exception as e:
        messages.add_message(request, messages.ERROR, 'There was some error updating record.')
        url = request.POST.get("download_url")
        return render(request, "edit_customer.html", {"user": user, "form": form, "url": url})
        # return redirect("edit-user", id="u-" + str(user.id))
        # return redirect("userListPage")

    messages.add_message(request, messages.SUCCESS, 'User updated successfully.')
    return redirect("edit-user", id="u-" + str(user.id))
    # return redirect("userListPage")


def update_degrees(form, request):
    degree_fields = filter(lambda x: "degree" in x, form.fields.keys())

    degrees = []
    for degree_field in degree_fields:
        val = request.POST.get(degree_field)
        if val:
            degrees.append(val.strip())

    for degree in degrees:
        try:
            if Degree.objects.filter(name=degree):
                continue
            obj = Degree(name=degree, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_college(form, request):
    college_fields = filter(lambda x: "college" in x, form.fields.keys())

    colleges = []
    for college_field in college_fields:
        val = request.POST.get(college_field)
        if val:
            colleges.append(val.strip())

    for college in colleges:
        try:
            if College.objects.filter(name=college):
                continue
            obj = College(name=college, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_company(form, request):
    company_fields = filter(lambda x: "company" in x, form.fields.keys())

    companies = []
    for college_field in company_fields:
        val = request.POST.get(college_field)
        if val:
            companies.append(val.strip())

    for company in companies:
        try:
            if Company.objects.filter(name=company):
                continue
            obj = Company(name=company, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_skill(form, request):
    skill_fields = filter(lambda x: "skill" in x, form.fields.keys())

    skills = []
    for skill_field in skill_fields:
        val = request.POST.get(skill_field)
        if val:
            skills.append(val.strip())

    for skill in skills:
        try:
            if Skill.objects.filter(name=skill):
                continue
            obj = Skill(name=skill, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_course(form, request):
    course_fields = filter(lambda x: "course" in x, form.fields.keys())

    courses = []
    for course_field in course_fields:
        val = request.POST.get(course_field)
        if val:
            courses.append(val.strip())

    for course in courses:
        try:
            if Course.objects.filter(name=course):
                continue
            obj = Course(name=course, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_industry(form, request):
    industry_fields = filter(lambda x: "industry" in x, form.fields.keys())

    industries = []
    for industry_field in industry_fields:
        val = request.POST.get(industry_field)
        if val:
            industries.append(val.strip())

    for industry in industries:
        try:
            if Industry.objects.filter(name=industry):
                continue
            obj = Industry(name=industry, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


def update_functional_area(form, request):
    functional_area_fields = filter(lambda x: "functional_area" in x, form.fields.keys())

    functional_areas = []
    for functional_area in functional_area_fields:
        val = request.POST.get(functional_area)
        if val:
            functional_areas.append(val.strip())

    for functional_area in functional_areas:
        try:
            if FunctionalArea.objects.filter(name=functional_area):
                continue
            obj = FunctionalArea(name=functional_area, created_by=request.user.email)
            obj.save()
        except Exception as e:
            print("There was some error " + str(e))


class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = Customer

    # define the columns that will be returned
    columns = ['id', 'email', 'name', 'skills', 'company', 'designation', 'current location',
               'preferred location', 'degree', 'experience', 'gender', 'industry']

    template_name = 'customer_list.html'  # Specify your own template name/location

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['id', 'email', 'name', '', 'company', '']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):

        if column == "id":
            return str(row.id)

        if column == 'degree':
            return ", ".join(filter(None, [row.ug_degree, row.pg_degree, row.additional_degree]))

        if column == 'name':
            return row.first_name + " " + row.last_name

        if column == 'skills':
            return ", ".join(filter(None, [row.primary_skills, row.secondary_skills]))

        if column == 'company':
            return row.current_company

        if column == 'designation':
            return row.current_designation

        if column == 'experience':
            return str(row.total_experience)

        if column == 'current location':
            return str(row.current_location)

        if column == 'preferred location':
            return str(row.preferred_location)

        return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # more advanced example using extra parameters
        degree_filter = self.request.GET.get("degree", None)
        skill_filter = self.request.GET.get("skill", None)
        location_filter = self.request.GET.get("location", None)
        exp_range_max = self.request.GET.get("exp_range[max]", None)
        exp_range_min = self.request.GET.get("exp_range[min]", None)
        search = self.request.GET.get("text", None)
        search_list = None
        if search:
            search_list = search.split(",")

        batch = self.request.GET.get("batch_id", None)
        batch = None if batch.lower() in ['none', 'all'] else batch

        degrees = degree_filter.split(',')
        skills = skill_filter.split(',')
        locations = location_filter.split(',')

        qs_params = None

        if degree_filter:
            degree_params = None
            for degree in degrees:
                q = Q(ug_degree__contains=degree) | Q(pg_degree__contains=degree)
                degree_params = degree_params | q if degree_params else q

            if qs_params:
                qs_params = qs_params & degree_params
            else:
                qs_params = degree_params

        if skill_filter:
            skill_params = None

            for skill in skills:
                q = Q(primary_skills__contains=skill) | Q(secondary_skills__contains=skill)
                skill_params = skill_params | q if skill_params else q

            if qs_params:
                qs_params = qs_params & skill_params
            else:
                qs_params = skill_params

        if location_filter:
            location_params = None

            for location in locations:
                q = Q(preferred_location__contains=location)
                location_params = location_params | q if location_params else q

            if qs_params:
                qs_params = qs_params & location_params
            else:
                qs_params = location_params

        if int(exp_range_max) != 0 and int(exp_range_min) != 0:
            exp_params = Q(total_experience__gte=exp_range_min) & Q(
                total_experience__gte=exp_range_max)

            if qs_params:
                qs_params = qs_params & exp_params
            else:
                qs_params = exp_params

        if search:
            search_params = None

            for search_item in search_list:
                q = Q(email__contains=search_item) | Q(resume_text__contains=search_item)
                search_params = search_params | q if search_params else q

            if qs_params:
                qs_params = qs_params | search_params
            else:
                qs_params = search_params

        if batch:
            batch_params = Q(batch_id=batch)
            if qs_params:
                qs_params = qs_params & batch_params
            else:
                qs_params = batch_params

        if qs_params:
            qs_params = qs_params & Q(is_staff=False)  # we don't want to show staff users here
        else:
            qs_params = Q(is_staff=False)

        if qs_params:
            qs = qs.filter(qs_params)

        return qs

    def ordering(self, qs):
        """ Get parameters from the request and prepare order by clause
        """

        # Number of columns that are used in sorting
        sorting_cols = 0
        if self.pre_camel_case_notation:
            try:
                sorting_cols = int(self._querydict.get('iSortingCols', 0))
            except ValueError:
                sorting_cols = 0
        else:
            sort_key = 'order[{0}][column]'.format(sorting_cols)
            while sort_key in self._querydict:
                sorting_cols += 1
                sort_key = 'order[{0}][column]'.format(sorting_cols)

        order = []
        order_columns = self.get_order_columns()

        for i in range(sorting_cols):
            # sorting column
            sort_dir = 'asc'
            try:
                if self.pre_camel_case_notation:
                    sort_col = int(self._querydict.get('iSortCol_{0}'.format(i)))
                    # sorting order
                    sort_dir = self._querydict.get('sSortDir_{0}'.format(i))
                else:
                    sort_col = int(self._querydict.get('order[{0}][column]'.format(i)))
                    # sorting order
                    sort_dir = self._querydict.get('order[{0}][dir]'.format(i))
            except ValueError:
                sort_col = 0

            sdir = '-' if sort_dir == 'desc' else ''
            sortcol = order_columns[sort_col]

            # hack to get custom columns ordering working
            if sortcol == 'name':
                sortcol = ['first_name', 'last_name']

            if sortcol == 'company':
                sortcol = 'current_company'

            if sortcol == 'id':
                sortcol = 'id'

            if isinstance(sortcol, list):
                for sc in sortcol:
                    order.append('{0}{1}'.format(sdir, sc.replace('.', '__')))
            else:
                order.append('{0}{1}'.format(sdir, sortcol.replace('.', '__')))

        if order:
            return qs.order_by(*order)
        return qs


@login_required(login_url='/accounts/login/')
@group_required(group_names=["data-entry operator"], redirect_url='/unauthorized/')
def data_entry_page(request):
    return HttpResponse("Entry restricted only for data entry operator group")


@login_required(login_url='/accounts/login/')
@group_required(group_names=["casual group"], redirect_url='/unauthorized/')
def user_view(request):
    return HttpResponse("Restricted end-user view")


def unauthorized(request):
    return HttpResponse("Unauthorized")
