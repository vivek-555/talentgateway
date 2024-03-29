from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField

states_and_uts = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
                  'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu',
                  'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir',
                  'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh',
                  'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
                  'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                  'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Not Available']
STATE_CHOICES = map(lambda x: (x, x), states_and_uts)


# Create your models here.
class Customer(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('-', 'Not Available'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='-')
    secondary_email = models.EmailField(max_length=70, blank=True, null=True)
    dob = models.DateField(default=datetime.now, blank=True, null=True)
    mobile = models.CharField(max_length=256, blank=True, null=True)
    secondary_mobile = models.CharField(max_length=256, blank=True, null=True)

    ug_degree = models.CharField(max_length=256, blank=True, null=True)
    ug_completion_year = models.IntegerField(null=True, blank=True)
    ug_college = models.CharField(max_length=256, blank=True, null=True)
    ug_course = models.CharField(max_length=256, blank=True, null=True)

    pg_degree = models.CharField(max_length=256, blank=True, null=True)
    pg_completion_year = models.IntegerField(null=True, blank=True)
    pg_college = models.CharField(max_length=256, blank=True, null=True)
    pg_course = models.CharField(max_length=256, blank=True, null=True)

    additional_degree = models.CharField(max_length=256, blank=True, null=True)
    additional_completion_year = models.IntegerField(null=True, blank=True)
    additional_college = models.CharField(max_length=256, blank=True, null=True)
    additional_course = models.CharField(max_length=256, blank=True, null=True)

    total_experience = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=19)

    current_company = models.CharField(max_length=256, blank=True, null=True)
    current_location = models.CharField(max_length=256, blank=True, null=True,
                                        choices=STATE_CHOICES)
    current_salary = models.IntegerField(null=True, blank=True)
    current_designation = models.CharField(max_length=256, blank=True, null=True)
    current_exprience = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=19)

    industry = models.CharField(max_length=256, blank=True, null=True)

    primary_skills = models.CharField(max_length=256, blank=True, null=True)
    secondary_skills = models.CharField(max_length=256, blank=True, null=True)

    current_functional_area = models.CharField(max_length=256, blank=True, null=True)
    notice_period = models.IntegerField(null=True, blank=True)

    preferred_location = models.CharField(max_length=256, blank=True, null=True,
                                          choices=STATE_CHOICES)
    preferred_salary = models.IntegerField(null=True, blank=True)
    preferred_functional_area = models.CharField(max_length=256, blank=True, null=True)
    preferred_industry = models.CharField(max_length=256, blank=True, null=True)

    resume_url = models.TextField(null=True, blank=True)
    resume_text = models.TextField(null=True, blank=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object

    batch_id = models.TextField(null=True, blank=True)

    applied_to = models.TextField(null=True, blank=True)
    source = models.TextField(null=True, blank=True)
    application_date = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email


class Tag(models.Model):
    user = models.ManyToManyField(Customer)
    name = models.CharField(max_length=256, blank=False, null=False)
    value = models.CharField(max_length=256, blank=False, null=False)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class FunctionalArea(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    alias = models.CharField(max_length=256, blank=True, null=True)

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Filter(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    data = JSONField()

    user = models.ManyToManyField(Customer, blank=True)

    TYPE_CHOICES = (
        ('Global', 'Global'),
        ('Local', 'Local'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Local")

    created_by = models.EmailField(max_length=70, blank=True, null=True)  # who created the object
    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.name


class Job(models.Model):
    job_id = models.CharField(max_length=10, blank=True, null=True)
    posted_by = models.CharField(max_length=256, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    target_exp = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=19)
    min_salary = models.IntegerField(null=True, blank=True)
    max_salary = models.IntegerField(null=True, blank=True)
    salary_text = models.CharField(max_length=256, blank=True, null=True)
    tag = models.CharField(max_length=256, blank=True, null=True)
    functional_area = models.CharField(max_length=256, blank=True, null=True)
    industry = models.CharField(max_length=256, blank=True, null=True)

    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.job_id + " - " + self.title




class JobApplicant(models.Model):
    job = models.ManyToManyField(Job)

    name = models.CharField(max_length=256, blank=False, null=False)
    email = models.EmailField(max_length=70, blank=False, null=False)
    mobile = models.CharField(max_length=256)
    resume_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)

    created_at = models.DateTimeField(
            auto_now_add=True)  # This should add the created date on its own only once.
    updated_at = models.DateTimeField(
            auto_now=True)  # This should add the updated date every time.

    def __str__(self):
        return self.email

    def applied_jobs(self):
        return ", ".join([p.job_id for p in self.job.all()])
