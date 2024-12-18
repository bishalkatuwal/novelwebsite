from typing import Any
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from django.urls import reverse



class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    author_pic = models.ImageField(upload_to='author_pic', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Novel(models.Model):
    CATEGORY_CHOICES = [
        ('popular', 'Popular'),
        ('latest', 'Latest'),
        ('completed', 'Completed'),
        ('featured', 'Featured'),
        
    ]
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name='light_novels')
    slug = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    cover_image = models.ImageField(upload_to='novel/novel_pic/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='popular')

    def __str__(self):
        return self.title


class ReadingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'novel')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username}'s list - {self.novel.title}"







class Volume(models.Model):
    novel = models.ForeignKey(Novel, related_name='volumes', on_delete=models.CASCADE)
    volume = models.PositiveIntegerField(default=0)
    novel_pdf = models.FileField(upload_to='novels/pdf/', blank=True, null=True)

    def __str__(self):
        return f"{self.novel.title} - Volume {self.volume}"

    def get_pdf_url(self):
        if self.novel_pdf:
            return self.novel_pdf.url
        return None




    


class Contacts(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.PositiveIntegerField(null=True, blank=True)
    novel_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    messages = models.TextField()


    def __str__(self):
        return self.full_name
    

    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Making the user field non-nullable
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='reviews')  # Removed default
    comment = models.TextField(default='Add Comment')
    rating = models.PositiveIntegerField(blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating} stars"
    



class Page(models.Model):
    STATUS_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public')
    ]
    title=models.CharField(max_length=100)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    slug=models.SlugField(max_length=200, blank=True, unique=True)
    summary = FroalaField(blank=True, null=True)
    description = FroalaField(blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_keyword = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='private')

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])


    def __str__(self):
        return self.title

    



class ChildPage(models.Model):
    parent = models.ForeignKey('Page', related_name='child_pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = FroalaField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title