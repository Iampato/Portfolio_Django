from .models import subscriber
from django import forms

class subscribeForm(forms.ModelForm):
	class Meta:
		model = subscriber
		
		Name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Full Name' } ))
		Email = forms.EmailField(required=True,  widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email' } ))

		fields = ('Name','Email')