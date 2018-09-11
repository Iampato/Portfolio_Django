from django.forms import ModelForm
from django import forms
from .models import Message

# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Full Name'
        }
    ))
    Phone = forms.CharField(max_length=10,  widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Phone'
        }
    ))
    Email = forms.EmailField(required=True,  widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email'
        }
    ))
    Message = forms.CharField(required=True,widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Message',
            'rows' : '4'
        } 
    ))

class messageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('Name','Phone', 'Email', 'Message')
        


