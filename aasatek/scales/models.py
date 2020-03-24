from django.db import models

# Create your models here.
class Scales(models.Model):
  race                  = models.IntegerField()
  carNum                = models.IntegerField()
  preQualifingWeight    = models.IntegerField()
  preQualifingLeft      = models.IntegerField()
  raceStartWeight       = models.IntegerField()
  raceStartLeft         = models.IntegerField()
  midRaceStart          = models.IntegerField()
  midRaceLeft           = models.IntegerField()

  def __str__(self):
    return self.carNum
