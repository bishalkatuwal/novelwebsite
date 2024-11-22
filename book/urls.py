
from django.urls import path
from .views import HomeView, LightNovelView,ContactView, NovelDetailView, AddReviewView, CategoryNovelListView




urlpatterns = [
   

   path('', HomeView.as_view(), name='home'),
   path('popular/', CategoryNovelListView.as_view(), {'category': 'popular'}, name='popular_novels'),
   path('completed/', CategoryNovelListView.as_view(), {'category': 'completed'}, name='completed_novels'),
   path('new/', CategoryNovelListView.as_view(), {'category': 'new'}, name='new_novels'),
   path('featured/', CategoryNovelListView.as_view(), {'category': 'featured'}, name='featured_novels'),
   path('category/<str:category>/', CategoryNovelListView.as_view(), name='category_novels'),
   path('lightnovel/', LightNovelView.as_view(), name='novels'),
   path('contact/', ContactView.as_view(), name='contact'),
   path('<slug:slug>/', NovelDetailView.as_view(), name='novel_detail'),
   path('<slug:slug>/add-review/', AddReviewView.as_view(), name='add-review'),



]
