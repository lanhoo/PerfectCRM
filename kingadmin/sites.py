from kingadmin.admin_base import BaseKingAdmin


class AdminSite(object):
    def __init__(self):
        self.enable_admin = {}

    def register(self, model_class, admin_class=None):
        app_name = model_class._meta.app_label
        model_name = model_class._meta.model_name
        if not admin_class:
            admin_obj = BaseKingAdmin()
        else:
            admin_obj = admin_class()

        admin_obj.model = model_class
        if app_name not in self.enable_admin:
            self.enable_admin[app_name] = {}
        self.enable_admin[app_name][model_name] = admin_obj

site = AdminSite()