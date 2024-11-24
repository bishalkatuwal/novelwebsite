from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Novel, Contacts, Review, ReadingList
from .forms import ContactForm, ReviewForm
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View




class HomeView(ListView):
    model = Novel
    template_name = 'home.html'
    context_object_name = 'novels'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_novels'] = Novel.objects.filter(category='popular')[:10]
        context['completed_novels'] = Novel.objects.filter(category='completed')[:10]
        context['new_novels'] = Novel.objects.filter(category='new')[:10]
        context['featured_novels'] = Novel.objects.filter(category='featured')[:10]

        # Add the category URLs
        
        context['popular_novels_url'] = reverse('popular_novels')
        context['completed_novels_url'] = reverse('completed_novels')
        context['new_novels_url'] = reverse('new_novels')
        context['featured_novels_url'] = reverse('featured_novels')


        return context




class CategoryNovelListView(ListView):
    model = Novel
    template_name = 'category_novels.html'
    
    def get_queryset(self):
        category = self.kwargs['category']
        return Novel.objects.filter(category=category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs['category']
        context['category_name'] = category.capitalize()  # Capitalize category name for the header
        return context





class LightNovelView(ListView):
    model = Novel
    template_name = 'light_novel.html'
    context_object_name = 'novels'



    def get_queryset(self):
    # Retrieve the query parameter
        query = self.request.GET.get('q', '').strip()  # Use .strip() to remove extra spaces
        if query:
        # Filter novels based on the query
            return Novel.objects.filter(
            Q(title__icontains=query)
        )
        return Novel.objects.all()  # Default queryset


    def get_context_data(self, *args, **kwargs):
        context  =super(LightNovelView,self).get_context_data( *args, **kwargs)

        context['query'] = self.request.GET.get('q', '')


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
    




class AddToListView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Fetch the novel based on the novel_id from the URL
        novel = get_object_or_404(Novel, id=self.kwargs['novel_id'])

        # Check if the novel is already in the user's reading list
        if ReadingList.objects.filter(user=self.request.user, novel=novel).exists():
            messages.info(request, "This novel is already in your reading list.")
        else:
            # Add the novel to the user's reading list
            ReadingList.objects.create(user=request.user, novel=novel)
            messages.success(request, f"'{novel.title}' has been added to your reading list.")

        # Redirect back to the novel detail page or the reading list
        return redirect('reading_list')



class ReadingListView(LoginRequiredMixin, ListView):
    model = ReadingList
    template_name = 'reading_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reading_list'] = self.get_queryset()
        return context

class RemoveFromListView(View):
    def post(self, request, item_id):
        # Use get_object_or_404 instead of get_list_or_404
        reading_item = get_object_or_404(ReadingList, id=item_id)
        
        # Delete the reading item from the list
        reading_item.delete()

        # Redirect to the reading list page after removing the item
        return redirect('reading_list')