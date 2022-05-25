from django.urls import re_path
from django.urls import URLPattern 

from . import views
app_name = "students_app"

urlpatterns = [

    re_path(r'^$', views.index, name = 'index'),
    #regular expression for students_app/7/
    re_path(r'^(?P<id>[0-9]+)/$', views.detail, name ='detail'),

    re_path(r'^details/(?P<id>[0-9]+)/$',views.detail, name='details'),
]