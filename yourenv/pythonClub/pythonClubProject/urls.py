from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('getResources/', views.getResources, name='resource'),
    path('getEvents/', views.getEvents, name='event'),
    path('meetingDetails/<int:id>', views.meetingDetails, name='meetingDetails'),
    path('newMeeting/', views.newMeeting, name='newMeeting'),
    path('newMeetingMinutes/', views.newMeetingMinutes, name='newMeetingMinutes'),
    # path('getMeetingMinutes/', views.getMeetingMinutes, name='meeting_Minutes'),
]
