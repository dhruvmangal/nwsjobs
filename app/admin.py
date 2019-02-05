# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Job, Jobseeker, Skills, JobCategory, College, College_details, College_event, Company, Plans

# Register your models here.
admin.site.register(Job)
admin.site.register(Jobseeker)
admin.site.register(Skills)
admin.site.register(JobCategory)
admin.site.register(College)
admin.site.register(College_details)
admin.site.register(College_event)
admin.site.register(Company)
admin.site.register(Plans)
