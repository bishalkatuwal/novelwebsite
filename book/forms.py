from django import forms
from .models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['full_name', 'email', 'number' ,'novel_name', 'author', 'messages']  # Correct field names
