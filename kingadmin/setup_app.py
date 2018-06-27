from django.conf import settings
# from PerfectCRM import settings
import importlib


def kingadmin_auto_discover():
    for app in settings.INSTALLED_APPS:
        # print(app)
        try:
            importlib.import_module('%s.kingadmin' %app)
        except Exception as e:
            # print(e)
            pass