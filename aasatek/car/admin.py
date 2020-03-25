from django.contrib import admin

# Register your models here.
from .models import Car

class CarAdmin(admin.ModelAdmin):
  list_display = ['carNum', 'driver', 'division', 'is_racing']
  list_editable = ['is_racing']

admin.site.register(Car, CarAdmin)