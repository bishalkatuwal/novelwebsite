from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Novel, Contacts
from .forms import ContactForm
from django.urls import reverse_lazy




class HomeView(ListView):
    model = Novel
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context  =super(HomeView,self).get_context_data( *args, **kwargs)
        return context


class LightNovelView(ListView):
    model = Novel
    template_name = 'light_novel.html'

    def get_context_data(self, *args, **kwargs):
        context  =super(LightNovelView,self).get_context_data( *args, **kwargs)
        return context



class NovelDetailView(DetailView):
    model = Novel
    template_name = 'novel_details.html'
    context_object_name = 'novel'

   







class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context  =super(ContactView,self).get_context_data( *args, **kwargs)
        return context




   
    