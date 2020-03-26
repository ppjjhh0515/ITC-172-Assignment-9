from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
        type=Meeting(meetingtitle='Weekly team meeting')
        self.assertEqual(str(type), type.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting Name')
    
class MeetingMinutesTest(TestCase):
    def test_string(self):
        type=MeetingMinutes(minutename='Interview Session')
        self.assertEqual(str(type), type.minutename)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'Minute Name')
 
class ResourceTest(TestCase):
    def test_string(self):
        type=Resource(resourcename='zoom')
        self.assertEqual(str(type), type.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_string(self):
        type=Event(eventtitle='Board meeting')
        self.assertEqual(str(type), type.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')
