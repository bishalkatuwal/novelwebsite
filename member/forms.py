from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ('username', 'first_name',  'last_name' , 'email', 'password1', 'password2')



class ProfileCreationForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ['profile_pic','user', 'bio']




class CustomUSerForm(UserCreationForm):

    class Meta:

        model = get_user_model()
        fields = ['first_name', 'last_name', 'username' ,'email', 'password1', 'password2']