from django.db import models

# Create your models here.
class Saftey(models.Model):
  carNum            = models.CharField(max_length=3)
  division          = models.CharField(max_length=20)
  helmetDate        = models.CharField(max_length=20)
  seatbeltDate      = models.CharField(max_length=20)
  windowNet         = models.CharField(max_length=20)
  headAndNeck       = models.CharField(max_length=20)
  fireSuite         = models.CharField(max_length=20)
  gloves            = models.CharField(max_length=20)
  shoes             = models.CharField(max_length=20)
  seat              = models.CharField(max_length=20)
  firesystem        = models.CharField(max_length=20)
  radio             = models.CharField(max_length=20)
  transponder       = models.CharField(max_length=20)
  drivelineLoop     = models.CharField(max_length=20)
  sideExhaust       = models.CharField(max_length=20)
  masterKill        = models.CharField(max_length=20)
  fuelLines         = models.CharField(max_length=20)
  fuelCellHeight    = models.CharField(max_length=20)
  colapsableCoulum  = models.CharField(max_length=20)
  cage              = models.CharField(max_length=20)
  weightBlocks      = models.CharField(max_length=20)
  drivelinepainted  = models.CharField(max_length=20)
  notes             = models.TextField(max_length=20)
  recheck           = models.TextField(max_length=20, default='False')

  def __str__(self):
    return self.carNum