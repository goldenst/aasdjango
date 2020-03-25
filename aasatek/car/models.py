from django.db import models


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
class Car(models.Model):
  carNum              = models.CharField(max_length=4)
  division            = models.CharField(max_length=20, choices=DIVISION_CHOICES)
  engine              = models.CharField(max_length=20, null=True, blank=True)
  driver              = models.CharField(max_length=100, null=True, blank=True)
  carMake             = models.CharField(max_length=100, null=True, blank=True)
  requiredWeight      = models.IntegerField(null=True, blank=True)
  minleftSideWeight   = models.DecimalField(decimal_places=1, max_digits=4, null=True, blank=True)
  carOwner            = models.CharField(max_length=100, null=True, blank=True)
  messageNumber       = models.CharField(max_length=11, null=True, blank=True)
  is_racing           = models.BooleanField(default=False)

  def __str__(self):
    return self.carNum