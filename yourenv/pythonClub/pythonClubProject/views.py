from django.shortcuts import render, get_object_or_404
from .models import Meeting, Meeting_Minutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm
#may need to remove meeting details from imports
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
    return render(request, 'pythonClubProject/events.html',{'meeting_list' : meeting_list})

def meetingDetails(request, id):
    meet=get_object_or_404(Meeting_Minutes, pk=id)
    return render(request, 'pythonClubProject/meetingDetails.html', {'meet': meet})

def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'pythonClubProject/newMeeting.html', {'form': form})

def newMeetingMinutes(request):
     form=MeetingMinutesForm
     if request.method=='POST':
          form=MeetingMinutesForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingMinutesForm()
     return render(request, 'pythonClubProject/newMeetingMinutes.html', {'form': form})