from django.conf import settings
from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
  ('pass', 'Pass'),
  ('fail', 'Fail'),
)

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

RECHECK_CHOICES = (
  ('Yes', 'Yes'),
  ('No', 'No')
)

HELMET_CHOICES = (
  ('SA2012', 'SA2020'),
  ('SA2015', 'SA2015'),
  ('SA2010', 'SA2010'),
  ('Out Datad', 'Out Dated')
)


User = settings.AUTH_USER_MODEL
# Create your models here.
class Saftey(models.Model):
  
  carNum            = models.CharField(max_length=3)
  division          = models.CharField(max_length=20, choices=DIVISION_CHOICES)
  helmetDate        = models.CharField(max_length=20, choices=HELMET_CHOICES)
  seatbeltDate      = models.CharField(max_length=20)
  windowNet         = models.CharField(max_length=20, choices=STATUS_CHOICES)
  headAndNeck       = models.CharField(max_length=20, choices=STATUS_CHOICES)
  fireSuite         = models.CharField(max_length=20, choices=STATUS_CHOICES)
  gloves            = models.CharField(max_length=20, choices=STATUS_CHOICES)
  shoes             = models.CharField(max_length=20, choices=STATUS_CHOICES)
  seat              = models.CharField(max_length=20, choices=STATUS_CHOICES)
  firesystem        = models.CharField(max_length=20, choices=STATUS_CHOICES)
  radio             = models.CharField(max_length=20, choices=STATUS_CHOICES)
  transponder       = models.CharField(max_length=20, choices=STATUS_CHOICES)
  drivelineLoop     = models.CharField(max_length=20, choices=STATUS_CHOICES)
  sideExhaust       = models.CharField(max_length=20, choices=STATUS_CHOICES)
  masterKill        = models.CharField(max_length=20, choices=STATUS_CHOICES)
  fuelLines         = models.CharField(max_length=20, choices=STATUS_CHOICES)
  fuelCellHeight    = models.CharField(max_length=20, choices=STATUS_CHOICES)
  colapsableCoulum  = models.CharField(max_length=20, choices=STATUS_CHOICES)
  cage              = models.CharField(max_length=20, choices=STATUS_CHOICES)
  weightBlocks      = models.CharField(max_length=20, choices=STATUS_CHOICES)
  drivelinepainted  = models.CharField(max_length=20, choices=STATUS_CHOICES)
  notes             = models.TextField(blank=True, null=True)
  recheck           = models.CharField(max_length=20, default='No', choices=RECHECK_CHOICES )
  User              = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
  created_at        = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.carNum
  
  def get_absolute_url(self):
    return reverse('saftey:detail', kwargs={'pk': self.pk})