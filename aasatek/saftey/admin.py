from django.contrib import admin

# Register your models here.
admin.site.site_header = "AAS Track Tek "
admin.site.site_title = "Admin -- AAS Track Tek"
admin.site.index_title = " AAS Track Tek Admin Area"

from .models import Saftey

admin.site.register(Saftey)