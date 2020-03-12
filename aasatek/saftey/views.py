from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Saftey
from .forms import SafteyFormA


def saftey_list_view(request):
    queryset = Saftey.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'saftey/list.html', context)


#  Create Safty Sheet-----------------------------------------
def createSaftey(request):
    form = SafteyFormA(request.POST or None) 
    if form.is_valid():
        form.save()
        form = SafteyFormA()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'saftey/saftey_create.html', context)


# Update view -----------------------------------------------


def saftey_update_view(request, pk=None, *args, **kwargs):
    form = SafteyForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'saftey/update.html', context)
