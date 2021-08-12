from django.urls import path
from app1.views import *
app_name='ashu'

urlpatterns=[
    path('app1_fun1/',app1_fun1,name='app1_fun1'),
]