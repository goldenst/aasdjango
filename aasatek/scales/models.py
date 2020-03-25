from django.conf import settings
from django.db import models
from django.urls import reverse

DIVISION_CHOICES = (
  ('Latemodel', 'Latemodel'),
  ('Jr latemodel', 'Jr latemodel'),
  ('Limited modifieds', 'Limited modifieds'),
  ('Super Stock', 'Super Stock'),
  ('F4', 'F4'),
  ('Mini Cup / Bandoleros', 'Mini Cup / Bandoleros'),
  ('Trailer', 'Trailer'),
  ('UTV', 'UTV'),
  ('Enduro', 'Enduro'),
)

# Create your models here.
class Scales(models.Model):
  race                  = models.IntegerField()
  carNum                = models.CharField(max_length=4)
  division              = models.CharField(max_length=20, choices=DIVISION_CHOICES)
  preQualifingWeight    = models.IntegerField()
  preQualifingLeft      = models.DecimalField(decimal_places=1, max_digits=3)
  raceStartWeight       = models.IntegerField(blank=True, null=True)
  raceStartLeft         = models.DecimalField(decimal_places=1, max_digits=3, blank=True, null=True)
  midRaceStart          = models.IntegerField(blank=True, null=True)
  midRaceLeft           = models.DecimalField(decimal_places=1, max_digits=3,blank=True, null=True)
  created_at            = models.DateTimeField(auto_now_add=True)
  updated_at            = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.carNum

  def get_absolute_url(self):
    return reverse('scales:detail', kwargs={'pk': self.pk})
