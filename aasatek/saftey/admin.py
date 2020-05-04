from django.contrib import admin

# Register your models here.
admin.site.site_header = "AAS Track Tek "
admin.site.site_title = "Admin -- AAS Track Tek"
admin.site.index_title = " AAS Track Tek Admin Area"

from .models import Saftey


class SafteyAdmin(admin.ModelAdmin):
  list_display = ['carNum', 'created_at', 'division', 'recheck']


admin.site.register(Saftey, SafteyAdmin)

