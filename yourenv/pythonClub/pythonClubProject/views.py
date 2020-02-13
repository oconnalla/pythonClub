from django.shortcuts import render, get_object_or_404
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

def meetingDetails(request, id):
    meet=get_object_or_404(Meeting_Minutes, pk=id)
    return render(request, 'pythonClubApp/meetingDetails.html', {'meet': meet})