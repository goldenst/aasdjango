from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include



from aasatek.views import home_page, navar, login_page, register_page, RulesView

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('rules/', RulesView, name='rules'),
    path('register/', register_page, name='register'),
    path('cars/', include('car.urls', namespace='car')),
    path('saftey/', include('saftey.urls', namespace='saftey')),
    path('scales/', include('scales.urls', namespace='scales')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)