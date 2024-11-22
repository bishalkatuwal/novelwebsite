from django import forms
from .models import Contacts, Review


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['full_name', 'email', 'number' ,'novel_name', 'author', 'messages']  # Correct field names



class ReviewForm(forms.ModelForm):
    class Meta:

        model = Review
        fields = ['comment']

