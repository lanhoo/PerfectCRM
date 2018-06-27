from django.conf.urls import url
from crm import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^sales_dashboard$', views.index, name='sales_dashboard'),
]
