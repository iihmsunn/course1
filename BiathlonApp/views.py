# Create your views here.

from models import *
from django.shortcuts import render_to_response
from django.template import RequestContext
#from forms import QuestionsForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime

def home(request):
    events = Event.objects.all().order_by('-date')
    context = {
               'events': events,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]
               }
    return render_to_response(
        'home.html',
        context
    )

def tracks(request):
    tracks = Track.objects.all().order_by('name')
    context = {
               'tracks': tracks,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]
               }
    return render_to_response(
        'tracks.html',
        context
    )

def athletes(request):
    athletes = Athlete.objects.all().order_by('name')
    context = {
               'athletes': athletes,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]
               }
    return render_to_response(
        'athletes.html',
        context
    )


def event(request, id):
    event = Event.objects.get(id=id)
    results = []
    times = []
    if event.date < datetime.datetime.now(tz=timezone.get_default_timezone()):
        results = [(r, str(datetime.timedelta(seconds = r.time/100.0)))for r in event.result_set.all().order_by('time')]

    context = {
               'event': event,
               'results': results,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]
               }
    return render_to_response(
                              'event.html',
                              context
                              )

def track(request, id):
    track = Track.objects.get(id=id)
    context = {'track': track,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]}
    return render_to_response(
                              'track.html',
                              context
                              )

def athlete(request, id):
    athlete = Athlete.objects.get(id=id)
    context = {'athlete': athlete,
               'recent_events': Event.objects.all().filter(date__lte=datetime.datetime.utcnow()).order_by('-date')[:10],
               'upcoming_events': Event.objects.all().filter(date__gte=datetime.datetime.utcnow()).order_by('-date')[:10]}
    return render_to_response(
                              'athlete.html',
                              context
                              )

