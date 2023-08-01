from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name="add"),
    path('delete',views.delete,name="delete"),
    path('search',views.search,name="search"),
    path('view',views.view,name="view")
]
