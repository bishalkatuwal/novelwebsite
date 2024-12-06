from django.db import models
from django.contrib.auth.models import User


class WriterNovel(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    cover_img = models.ImageField(upload_to='writer/novel_cover_img')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    novel_pdf = models.FileField(upload_to='novels/pdf')


    def __str__(self):
        return self.title