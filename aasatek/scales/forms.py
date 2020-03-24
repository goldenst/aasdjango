from django import forms
from .models import Scales


class ScalesForm(forms.ModelForm):
  class Meta:
    model = Scales
    exclude = ['user']
    fields = '__all__'