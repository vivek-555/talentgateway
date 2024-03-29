import django.forms as forms
from django.forms import ModelForm
from models import *


class UserForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions',
                   'is_active', 'is_staff', 'username', 'date_joined', 'resume_url', 'created_by']

    id = forms.HiddenInput()

    email = forms.Field(disabled=True)

    ug_degree = forms.ModelChoiceField(queryset=Degree.objects.all(), to_field_name="name",
                                       empty_label="Not Available", required=False)
    pg_degree = forms.ModelChoiceField(queryset=Degree.objects.all(), to_field_name="name",
                                       empty_label="Not Available", required=False)
    additional_degree = forms.ModelChoiceField(queryset=Degree.objects.all(), to_field_name="name",
                                               empty_label="Not Available", required=False)

    ug_college = forms.ModelChoiceField(queryset=College.objects.all(), to_field_name="name",
                                        empty_label="Not Available", required=False)
    pg_college = forms.ModelChoiceField(queryset=College.objects.all(), to_field_name="name",
                                        empty_label="Not Available", required=False)
    additional_college = forms.ModelChoiceField(queryset=College.objects.all(),
                                                to_field_name="name", empty_label="Not Available",
                                                required=False)

    ug_course = forms.ModelChoiceField(queryset=Course.objects.all(), to_field_name="name",
                                       empty_label="Not Available", required=False)
    pg_course = forms.ModelChoiceField(queryset=Course.objects.all(), to_field_name="name",
                                       empty_label="Not Available", required=False)
    additional_course = forms.ModelChoiceField(queryset=Course.objects.all(), to_field_name="name",
                                               empty_label="Not Available", required=False)

    current_company = forms.ModelChoiceField(queryset=Company.objects.all(), to_field_name="name",
                                             empty_label="Not Available", required=False)

    industry = forms.ModelChoiceField(queryset=Industry.objects.all(), to_field_name="name",
                                      empty_label="Not Available", required=False)
    preferred_industry = forms.ModelChoiceField(queryset=Industry.objects.all(),
                                                to_field_name="name", empty_label="Not Available",
                                                required=False)

    primary_skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),
                                                    to_field_name="name", required=False)
    secondary_skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),
                                                      to_field_name="name", required=False)

    current_functional_area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(),
                                                     to_field_name="name",
                                                     empty_label="Not Available", required=False)
    preferred_functional_area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(),
                                                       to_field_name="name",
                                                       empty_label="Not Available", required=False)

    def clean_primary_skills(self):
        primary_skills = []
        for skill in self.cleaned_data['primary_skills']:
            primary_skills.append(str(skill))
        return ",".join(primary_skills)

    def clean_secondary_skills(self):
        secondary_skills = []
        for skill in self.cleaned_data['secondary_skills']:
            secondary_skills.append(str(skill))
        return ",".join(secondary_skills)


class JobApplicantForm(ModelForm):
    class Meta:
        model = JobApplicant
        exclude = ['job', 'resume_url']
