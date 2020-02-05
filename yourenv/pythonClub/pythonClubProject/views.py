from django.shortcuts import render
from .models import Meeting, Meeting_Minutes, Resource, Event 
# Create your views here.

def index (request):
    return render(request, 'pythonClubProject/index.html')

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonClubProject/meetings.html' ,{'meeting_list' : meeting_list})

def getMeetingMinutes(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonClubProject/meetingMinutes.html' ,{'meeting_list' : meeting_list})

def getResources(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonClubProject/resources.html' ,{'meeting_list' : meeting_list})

def getEvents(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonClubProject/events.html' ,{'meeting_list' : meeting_list})