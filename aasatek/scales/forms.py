from django import forms
from .models import Scales


class ScalesForm(forms.ModelForm):
  class Meta:
    model = Scales
    fields = '__all__'