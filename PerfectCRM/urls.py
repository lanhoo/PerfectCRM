from django.conf.urls import include, url
from django.contrib import admin
from PerfectCRM import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'PerfectCRM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.acc_login, name='login'),
    url(r'^logout/', views.acc_logout, name='logout'),

    url(r'^crm/', include('crm.urls')),
    url(r'^kingadmin/', include('kingadmin.urls')),
]
