from django.contrib import admin
from django.db.models.expressions import Func

from models import *


# Register your models here.

class CommonAdmin(admin.ModelAdmin):
    list_display = ("name", "alias", "created_by")


class JobAdmin(admin.ModelAdmin):
    list_display = ("job_id", "title", "target_exp", "functional_area", "industry", "posted_by")
    search_fields = ("job_id", "title", "functional_area", "industry", "posted_by")
    list_filter = ("title", "target_exp", "functional_area", "industry", "posted_by")


class JobApplicantAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "applied_jobs")
    search_fields = ("email", "name")
    list_filter = ["job"]


admin.site.register(Customer)
admin.site.register(College)
admin.site.register(Tag)
admin.site.register(Company, CommonAdmin)
admin.site.register(FunctionalArea, CommonAdmin)
admin.site.register(Skill, CommonAdmin)
admin.site.register(Course, CommonAdmin)
admin.site.register(Degree, CommonAdmin)
admin.site.register(Industry)
admin.site.register(Filter)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplicant, JobApplicantAdmin)
