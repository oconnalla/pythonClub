from django.test import TestCase
from .models import Meeting, Resource, Event, Meeting_Minutes
from .views import index, getMeetings, getResources, getEvents, meetingDetails, getMeetingMinutes, newMeeting
from .forms import MeetingForm
from django.urls import reverse
from django.contrib.auth.models import User


# Testing Models
#model 1 of 4
class MeetingTest(TestCase):
    def setUp(self):
       self.meet = Meeting(meeting_title='meetings', meeting_date='02/12/2020', meeting_time= '00:07:00', location = 'Renton, WA', agenda ='get budget in order')

    def test_string(self):
       #self.Meeting_title(name="meetings")
       self.assertEqual(str(self.meet), self.meet.meeting_title)  

    def test_date(self):
       self.assertEqual(self.meet.meeting_date, '02/12/2020')

    def test_time(self):
        self.assertEqual(self.meet.meeting_time, '00:07:00')

    def test_location(self):
       self.assertEqual(self.meet.location, 'Renton, WA')

    def test_agenda(self):
        self.assertEqual(self.meet.agenda, 'get budget in order')
 


 #model 2 of 4
 #having issues with many to many and foreign key relationships
class MinutesTest(TestCase):
    def setUp(self):
    #    meetID = meetingID.objects.create(meetingID = '1')
    #    self.meet = Meeting_Minutes(meetingID='1', attendance='1', minutes_text='blah')
        self.meet = Meeting_Minutes(minutes_text='blah')
    
    # def test_ID(self):
    #    self.assertEqual(self.meet.meetingID, '1')

    # def test_attendance(self):
    #     self.assertEqual(self.meet.attendance, '1')

    def test_minutes_text(self):
       self.assertEqual(self.meet.minutes_text, 'blah')


#model 3 of 4
class EventTest(TestCase):
    # def setUp(self):
    #    self.meet = Event(event_title='roof', location = 'Renton, WA', date='02/12/2020', time = '00:07:00', description ='blah', userID = '1')
    def setUp(self):
       self.meet = Event(event_title='roof', location = 'Renton, WA', date='02/12/2020', time = '00:07:00', description ='blah')

    def test_title(self):
       self.assertEqual(self.meet.event_title, 'roof')
       
    def test_Elocation(self):
       self.assertEqual(self.meet.location, 'Renton, WA')  

    def test_Edate(self):
       self.assertEqual(self.meet.date, '02/12/2020')

    def test_Etime(self):
        self.assertEqual(self.meet.time, '00:07:00')

    def test_description(self):
        self.assertEqual(self.meet.description, 'blah')
    
#     def test_userID(self):
#         self.assertEqual(self.meet.userID, '1')



#model 4 of 4
class ResourceTest(TestCase):
    def setUp(self):
       self.meet = Resource(resource_name='roof', resource_type = 'Renton, WA', url='www.imfailing.com', date_entered = '00:07:00', description ='blah')

    def test_resource_name(self):
       self.assertEqual(self.meet.resource_name, 'roof')
       
    def test_resource_type(self):
       self.assertEqual(self.meet.resource_type, 'Renton, WA')  

    def test_url(self):
       self.assertEqual(self.meet.url, 'www.imfailing.com')

    def test_date_entered(self):
        self.assertEqual(self.meet.date_entered, '00:07:00')

    def test_resource_description(self):
        self.assertEqual(self.meet.description, 'blah')

# TESTING VIEWS

class IndexTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('index'))
       self.assertEqual(response.status_code, 200) 

class GetResourceTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('resource'))
       self.assertEqual(response.status_code, 200)

class GetEventsTest(TestCase):
   def test_view_url_accessible_by_name(self):
       response = self.client.get(reverse('event'))
       self.assertEqual(response.status_code, 200)



#     def test_meeting_detail_success(self):
#         response = self.client.get(reverse('meetingDetails', args=(self.meet.id,)))
#         self.assertEqual(response.status_code, 200)

# def setUp(self):
#         self.u=User.objects.create(username='myuser')
#         self.type=Meeting_title.objects.create(typename='meetings')

        # self.meet = Meeting.objects.create(meeting_title='meetings', meeting_date='02/12/2020', meeting_time = '00:07:00', meeting_location = 'Renton, WA' meeting_agenda='get budget in order'
        # )
       
        # self.meet = Meeting_Minutes.objects.create(meetingID= '1', attendace = "1", minutes_text= "blah")




#Form tests

class MeetingType_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingForm(data={'meeting_title': "team Meeting", 'meeting_date' : "10/27/2020", 'meeting_time': "09:00:00", 'location': "Seattle", 'agenda': "get new staff onboarded"})
        self.assertTrue(form.is_valid())

    #second test asserts form is still valid when we leave out optional description field.
    def test_typeform_minus_descript(self):
        form=MeetingForm(data={'meeting_title': "team Meeting", 'meeting_date' : "10/27/2020", 'meeting_time': "09:00:00"})
        self.assertTrue(form.is_valid())
    
    #final test for form asserts that form will fail if we don't enter anything
    def test_typeform_empty(self):
        form=MeetingForm(data={'meeting_title': ""})
        self.assertFalse(form.is_valid())