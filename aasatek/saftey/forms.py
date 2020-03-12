from django import forms
# from django.contrib.auth import  get_user_model
from .models import Saftey

# User = get_user_model()

class SafteyFormA(forms.ModelForm):
  class Meta:
    model = Saftey
    fields = '__all__'


class SafteyForm(forms.Form):
    carNum = forms.CharField(
        label="Car Number",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Car Number"
            }
        )
    )
    division = forms.CharField(
        label="Division",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Division"
            }
        )
    )         
    helmetDate = forms.CharField(
        label="Helmet Date",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Helmet Date"
            }
        )
    )          
    seatbeltDate = forms.CharField(
        label="Seat Belts Date",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Seat Belts Date"
            }
        )
    )        
    windowNet = forms.CharField(
        label="Windoe net Date",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Windoe net Date"
            }
        )
    )           
    headAndNeck = forms.CharField(
        label="Head and Neck Device",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Head and Neck Device"
            }
        )
    )         
    fireSuite = forms.CharField(
        label="Firesuite ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Firesuite "
            }
        )
    )           
    gloves = forms.CharField(
        label="Has Gloves",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Has Gloves"
            }
        )
    )              
    shoes = forms.CharField(
        label="Has shoes",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Has shoes"
            }
        )
    )               
    seat = forms.CharField(
        label="Approved Seat",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Approved Seat"
            }
        )
    )                
    firesystem = forms.CharField(
        label="Fire Syatem",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Fire Syatem"
            }
        )
    )         
    radio = forms.CharField(
        label="Radio",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Radio"
            }
        )
    )               
    transponder = forms.CharField(
        label="Transponder",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Transponder"
            }
        )
    )         
    drivelineLoop = forms.CharField(
        label="Drive line Loop ",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Drive line Loop "
            }
        )
    )       
    sideExhaust = forms.CharField(
        label="Exhaust out Side",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Exhaust out Side"
            }
        )
    )         
    masterKill = forms.CharField(
        label="Master Kill Switch",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Master Kill Switch"
            }
        )
    )          
    fuelLines = forms.CharField(
        label="Fuel lines routed properley",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Fuel lines routed properley"
            }
        )
    )           
    fuelCellHeight = forms.CharField(
        label="Fuel Cell min Height",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Fuel Cell min Height"
            }
        )
    )      
    colapsableCoulum = forms.CharField(
        label="Cloapasable Steering Collumn",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Cloapasable Steering Collumn"
            }
        )
    )   
    cage = forms.CharField(
        label="RollCage good",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "RollCage good"
            }
        )
    )              
    weightBlocks = forms.CharField(
        label="Weight Blocks painted & Numbered",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Weight Blocks painted & Numbered"
            }
        )
    )      
    drivelinepainted = forms.CharField(
        label="Driveline painted White",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Driveline painted White"
            }
        )
    )  
    notes = forms.CharField(
        label="Noted",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "placeholder": "Noted"
            }
        )
    )             
    recheck = forms.CharField(
        label="Recheck Needed",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Recheck Needed"
            }
        )
    )