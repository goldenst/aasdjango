from django.db import models

# Create your models here.
class Saftey(models.Model):
  carNum            = models.CharField()
  division          = models.CharField()
  helmetDate        = models.CharField()
  seatbeltDate      = models.CharField()
  windowNet         = models.CharField()
  headAndNeck       = models.CharField()
  fireSuite         = models.CharField()
  gloves            = models.CharField()
  shoes             = models.CharField()
  seat              = models.CharField()
  firesystem        = models.CharField()
  radio             = models.CharField()
  transponder       = models.CharField()
  drivelineLoop     = models.CharField()
  sideExhaust       = models.CharField()
  masterKill        = models.CharField()
  fuelLines         = models.CharField()
  fuelCellHeight    = models.CharField()
  colapsableCoulum  = models.CharField()
  cage              = models.CharField()
  weightBlocks      = models.CharField()
  drivelinepainted  = models.CharField()
  notes             = models.TextField()