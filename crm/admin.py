from django.contrib import admin
from crm import models


admin.site.register(models.CustomInfo)
admin.site.register(models.CustomFollowUp)
admin.site.register(models.ClassList)
admin.site.register(models.Course)
admin.site.register(models.Branch)