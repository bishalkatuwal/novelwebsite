
from django.urls import path
from .views import RemoveFromListView,HomeView,ReadingListView,AddToListView,LightNovelView,ContactView, NovelDetailView, AddReviewView, CategoryNovelListView, PageView, PageDetailView



urlpatterns = [
     # Contact page
    path('contact/', ContactView.as_view(), name='contact'),


    
    # General pages
    path('', HomeView.as_view(), name='home'),
    path('page/', PageView.as_view(), name='page'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),  # Avoid conflict with other slugs

    # Category-specific views
    path('popular/', CategoryNovelListView.as_view(), {'category': 'popular'}, name='popular_novels'),
    path('completed/', CategoryNovelListView.as_view(), {'category': 'completed'}, name='completed_novels'),
    path('new/', CategoryNovelListView.as_view(), {'category': 'new'}, name='new_novels'),
    path('featured/', CategoryNovelListView.as_view(), {'category': 'featured'}, name='featured_novels'),
    path('category/<str:category>/', CategoryNovelListView.as_view(), name='category_novels'),

    # Novels and related actions
    path('lightnovel/', LightNovelView.as_view(), name='novels'),
    path('<slug:slug>/', NovelDetailView.as_view(), name='novel_detail'),
    path('<slug:slug>/add-review/', AddReviewView.as_view(), name='add_review'),

    # Reading list management
    path('reading-list/', ReadingListView.as_view(), name='reading_list'),
    path('add-to-list/<int:novel_id>/', AddToListView.as_view(), name='add_to_list'),
    path('remove-from-list/<int:item_id>/', RemoveFromListView.as_view(), name='remove_from_list'),

   
]
