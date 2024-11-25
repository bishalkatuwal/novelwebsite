from django.contrib import admin
from .models import Novel, Author, Genre, Volume, Contacts, Review, Page, ChildPage

# Register your models here.


admin.site.register(Novel)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Volume)
admin.site.register(Contacts)
admin.site.register(Review)
admin.site.register(Page)
admin.site.register(ChildPage)
