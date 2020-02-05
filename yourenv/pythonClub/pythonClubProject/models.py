from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Model 1 of 4
class Meeting(models.Model):
    meeting_title=models.CharField(max_length=255)
    meeting_date=models.DateField()
    meeting_time=models.TimeField()
    location=models.CharField(max_length=255, null=True, blank=True)
    agenda=models.CharField(max_length=255, null=True, blank=True)

    #NEED TO ADD METHODS###################
    def __str__(self):
        return self.meeting_title, self.meeting_date,self.meeting_time, self.location, self.agenda 
    
    class Meta:
        db_table='Meeting'
        verbose_name_plural='Meetings'


#Model 2 of 4
class Meeting_Minutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance = models.ManyToManyField(User)
    minutes_text=models.TextField()

    #NEED TO ADD METHODS###################
    def __str__(self):
        return self.meetingID, self.attendance, self.minutes_text
    
    class Meta:
        db_table='Meeting Minutes'
       # verbose_name_plural='Meeting Minutes'


#Model 3 of 4
class Resource(models.Model):
    resource_name=models.CharField(max_length=255, null=True, blank=True)
    resource_type=models.CharField(max_length=255, null=True, blank=True)
    url=models.URLField(null=True, blank=True)
    date_entered=models.DateField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()
    
    #NEED TO ADD METHODS###################
    def __str__(self):
        return self.resource_name, self.resource_type, self.url, self.date_entered, self.userID, self.description
    
    class Meta:
        db_table='Resource'
        verbose_name_plural='Resources'


#Model 4 of 4
class Event(models.Model):
    event_title=models.CharField(max_length=255)
    location=models.CharField(max_length=255, null=True, blank=True)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userID=models.ForeignKey(User, on_delete=models.DO_NOTHING)
        
    #NEED TO ADD METHODS###################
    def __str__(self):
        return self.event_title,self.location,self.date,self.time,self.description,self.userID
    
    class Meta:
        db_table='Event'
        verbose_name_plural='Events'
        