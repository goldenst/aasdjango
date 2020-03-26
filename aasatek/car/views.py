from django.views.generic import View, TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .forms import CarForm


class CarsListView(ListView):
    #   context name is car_list
    model = models.Car

class CarsDetailView(DetailView):
    context_object_name = 'car_detail'
    model = models.Car
    template_name = 'car/car_detail.html'

class CarsCreateView(CreateView):
    model = models.Car
    # form_class = SafteyForm
    exclude = ['user']
    fields = '__all__'
    template_name = 'car/car_create.html'

class CarsUpdateView(UpdateView):
    model = models.Car
    # form_class = SafteyForm
    
    fields = '__all__'
    exclude = ['user']
    template_name = 'car/car_create.html'

    

