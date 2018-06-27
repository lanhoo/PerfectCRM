from django.conf.urls import url
from kingadmin import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.acc_login, name='login'),
    url(r'^logout/', views.acc_logout, name='logout'),
]
