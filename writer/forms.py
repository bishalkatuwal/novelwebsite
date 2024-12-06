from django import forms
from .models import WriterNovel



class WriterNovelForm(forms.ModelForm):
    class Meta:
        model = WriterNovel
        fields = ['title', 'summary', 'cover_img', 'novel_pdf']
