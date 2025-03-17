from django import forms

from .models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),
        }


