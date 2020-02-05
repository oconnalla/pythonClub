from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getMeetingMinutes/', views.getMeetingMinutes, name='meeting_Minutes'),
    path('getResources/', views.getResources, name='resource'),
    path('getEvents/', views.getEvents, name='event'),
]
