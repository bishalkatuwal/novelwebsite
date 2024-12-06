from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import WriterNovelForm
from .models import WriterNovel
from django.views.generic import TemplateView




class WriterNovelCreateView(CreateView):
    model = WriterNovel
    form_class = WriterNovelForm
    template_name = 'novels/novel_form.html'
    success_url = reverse_lazy('writer_novels_list')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)



class WriterNovelsView(ListView):
    model = WriterNovel
    template_name = 'novels/novels.html'
    context_object_name = 'novels'

    def get_queryset(self):
        return WriterNovel.objects.all()
    

class WriterNovelDetailView(DetailView):
    model = WriterNovel
    template_name = 'novels/novel_detail.html'
    context_object_name = 'novel'




class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    login_url = '/login/'  # Redirect to login page if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['novels'] = WriterNovel.objects.filter(writer=user)
        return context