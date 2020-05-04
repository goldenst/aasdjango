from django.contrib import admin

# Register your models here.


from .models import Scales


class ScalesAdmin(admin.ModelAdmin):
  list_display = ['carNum', 'race', 'created_at', 'division']

admin.site.register(Scales, ScalesAdmin)