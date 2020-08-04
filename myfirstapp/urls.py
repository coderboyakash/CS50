from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('greet/<str:name>', views.greet, name="greet"),
    path('showpage', views.showpage, name='showpage'),
    path('getdata/<str:name>', views.getdata, name="getdata"),
    path('newyear', views.newyear, name="newyear"),
]