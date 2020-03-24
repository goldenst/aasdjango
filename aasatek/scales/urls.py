from django.urls import path
from scales import views

app_name = 'scales'

urlpatterns = [
    path('', views.ScalesListView.as_view(), name='list'),
    path('create/', views.ScalesCreateView.as_view(), name='create'),
    path('<pk>/', views.ScalesDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.ScalesUpdateView.as_view(), name='update')
]