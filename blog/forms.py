from django.forms import ModelForm
from django import forms
from .models import subscribe

# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Full Name'
        }
    ))
    Email = forms.EmailField(required=True,  widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email'
        }
    ))
    
class subscribeForm(forms.ModelForm):
    class Meta:
        model = subscribe
        fields = ('Name', 'Email')
        


