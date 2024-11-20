
from django.urls import path
from .views import HomeView, LightNovelView,ContactView, NovelDetailView, AddReviewView




urlpatterns = [
   

   path('', HomeView.as_view(), name='home'),
   path('lightnovel/', LightNovelView.as_view(), name='novels'),
   path('contact/', ContactView.as_view(), name='contact'),
   path('<slug:slug>/', NovelDetailView.as_view(), name='novel_detail'),
   path('<slug:slug>/add-review/', AddReviewView.as_view(), name='add-review'),



]
