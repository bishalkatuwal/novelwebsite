from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create your views here.



class RegistrationFormView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class ProfileUserView(CreateView):
     
    model = Profile
    fields = ['bio', 'profile_pic']
    template_name = 'profile/profile_create.html'
    success_url = reverse_lazy('profile/profile_detail')  # Redirect to profile detail page after creation

    def form_valid(self, form):
        # Link the profile to the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        # If the user already has a profile, redirect to profile detail page
        if Profile.objects.filter(user=request.user).exists():
            return redirect('profile_detail')
        return super().dispatch(request, *args, **kwargs)




class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    context_object_name = 'profile'


    def get_object(self, queryset=None):

        # Check if profile exists; if not, create it
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    


class ProfileEditView(UpdateView):
    model = Profile
    fields = ['bio', 'profile_pic']
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Fetch the profile of the logged-in user
        return self.request.user.profile
