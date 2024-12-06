from django.urls import path
from .views import WriterNovelCreateView, WriterNovelsView, WriterNovelDetailView


urlpatterns = [

    path('writer/novel/add/', WriterNovelCreateView.as_view(), name='novel_add'),
    path('writer/novel/list/', WriterNovelsView.as_view(), name='writer_novels_list' ),
    path('writer/novel/<int:pk>/', WriterNovelDetailView.as_view(), name='writer_novels_detail'),


]