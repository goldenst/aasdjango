from django.views.generic import View, TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .forms import ScalesForm


class ScalesListView(ListView):
    #   context name is saftey_list
    model = models.Scales

class ScalesDetailView(DetailView):
    context_object_name = 'scales_detail'
    model = models.Scales
    template_name = 'scales/scales_detail.html'

class ScalesCreateView(CreateView):
    model = models.Scales
    # form_class = SafteyForm
    exclude = ['user']
    fields = '__all__'
    template_name = 'scales/scales_create.html'

class ScalesUpdateView(UpdateView):
    model = models.Scales
    # form_class = ScalesForm
    
    fields = '__all__'
    exclude = ['user']
    template_name = 'scales/scales_create.html'

    