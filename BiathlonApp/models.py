from django.db import models

# Create your models here.
class Athlete(models.Model):
    country = models.CharField(max_length = 50)
    name = models.CharField(max_length = 250)
    info = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length = 250)
    length = models.FloatField()
    info = models.CharField(max_length = 1000)
    def __unicode__(self):
        return self.name

class Event(models.Model):
    track = models.ForeignKey(Track)
    name = models.CharField(max_length = 250)
    athletes = models.ManyToManyField(Athlete)
    info = models.CharField(max_length = 1000)
    date = models.DateTimeField()
    def __unicode__(self):
        return self.name

class Result(models.Model):
    event = models.ForeignKey(Event)
    athlete = models.ForeignKey(Athlete)
    shooting = models.CharField(max_length = 20)
    time = models.FloatField()
    def __unicode__(self):
        return self.athlete.__unicode__() + " - " + self.event.__unicode__()

class Championship:
    pass
