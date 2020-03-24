from django.urls import path
from saftey import views

app_name = 'saftey'

urlpatterns = [
    path('', views.SafteyListView.as_view(), name='list'),
    path('create/', views.SafteyCreateView.as_view(), name='create'),
    path('<pk>/', views.SafteyDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.SafteyUpdateView.as_view(), name='update')
]
