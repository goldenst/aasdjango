from django.views.generic import View, TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .forms import SafteyForm


class SafteyListView(ListView):
    #   context name is saftey_list
    model = models.Saftey

class SafteyDetailView(DetailView):
    context_object_name = 'saftey_detail'
    model = models.Saftey
    template_name = 'saftey/saftey_detail.html'

class SafteyCreateView(CreateView):
    model = models.Saftey
    # form_class = SafteyForm
    exclude = ['user']
    fields = '__all__'
    template_name = 'saftey/saftey_create.html'

class SafteyUpdateView(UpdateView):
    model = models.Saftey
    # form_class = SafteyForm
    
    fields = '__all__'
    exclude = ['user']
    template_name = 'saftey/saftey_create.html'

    