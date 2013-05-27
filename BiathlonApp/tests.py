"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from models import *

from django.test import TestCase
from django.utils import timezone
import datetime


class SimpleTest(TestCase):
    def test_result(self):
        """
        Tests event result query.
        """
    	track = Track(name = "Long track", length = 9000, info = "so long they are all going to die!")
        track.save()
        athlete1 = Athlete(country = "US", name = "Putin", info = "Master Of The Universe")
        athlete1.save()
        event_ = Event(track = track, name = "Very important race", info = "Very important race indeed!", date = datetime.datetime.utcnow())
		
        event_.save()
        result1 = Result(event = event_, athlete = athlete1, shooting = "1100110011", time = 9999)
        result1.save()
        event = Event.objects.get(id=1)
        results = [(r, str(datetime.timedelta(seconds = r.time/100.0)))for r in event.result_set.all().order_by('time')]
        self.assertEqual(results[0][1],str(datetime.timedelta(seconds = 9999/100.0)))
