from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Novel, Contacts, Review
from .forms import ContactForm, ReviewForm
from django.urls import reverse_lazy, reverse




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

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            novel = self.get_object()  # Get the novel using the slug
            context['reviews'] = novel.reviews.all()  # Get all reviews for this novel
            context['form'] = ReviewForm()  # Add the review form to the context
            return context

    def get_object(self, queryset=None):
            # Override to fetch by slug
            return get_object_or_404(Novel, slug=self.kwargs.get('slug'))







class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context  =super(ContactView,self).get_context_data( *args, **kwargs)
        return context



class AddReviewView(CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        novel = get_object_or_404(Novel, slug=self.kwargs['slug'])  # Fetch the novel using slug
        form.instance.novel = novel  # Associate the review with the correct novel
        form.instance.user = self.request.user  # Associate the review with the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('novel_detail', kwargs={'slug': self.object.novel.slug})