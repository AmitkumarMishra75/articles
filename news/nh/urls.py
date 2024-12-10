from django.urls import path
from . import views

urlpatterns = [
    path('',views.display, name='index'),
    path('1',views.about_me, name='about_me'),
    path('one/<int:pk>',views.display1,name='display1'),
]