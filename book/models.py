from typing import Any
from django.db import models
from django.utils import timezone


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
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name='light_novels')
    slug = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    published_date = models.DateField(default=timezone.now)
    cover_image = models.ImageField(upload_to='novel/novel_pic/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


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


