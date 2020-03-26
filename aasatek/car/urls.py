from django.urls import path
from car import views

app_name = 'car'

urlpatterns = [
    path('', views.CarsListView.as_view(), name='list'),
    path('create/', views.CarsCreateView.as_view(), name='create'),
    path('<pk>/', views.CarsDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.CarsUpdateView.as_view(), name='update')
]