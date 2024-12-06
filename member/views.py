from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import SignUpForm, CustomUSerForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from writer.models import WriterNovel
from book.models import ReadingList, Novel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

# Create your views here.



class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Middleware logic
        return self.get_response(request)



class RedirectAuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home page if logged in
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(CreateView):
    form_class = CustomUSerForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True



class UserLogoutView(LogoutView):
    next_page = 'home'




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
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['novels'] = WriterNovel.objects.filter(writer=user)
        return context
   




class ProfileEditView(UpdateView):
    model = Profile
    fields = ['bio', 'profile_pic']
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        # Fetch the profile of the logged-in user
        return self.request.user.profile





