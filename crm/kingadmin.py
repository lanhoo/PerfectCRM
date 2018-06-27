from kingadmin.sites import site
from kingadmin.admin_base import BaseKingAdmin
from crm import models


class CustomerAdmin(BaseKingAdmin):
    list_display = ['name', 'source', 'contact_type', 'contact', 'consultant', 'consult_content', 'status', 'date']
    list_filter = ['source', 'consultant', 'status', 'date']
    search_fields = ['contact', 'consultant__name']


print('kingadmin start crm .....')
site.register(models.CustomInfo, CustomerAdmin)
site.register(models.Role)
site.register(models.MenuUrl)
site.register(models.UserProfile)
