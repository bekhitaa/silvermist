from django.contrib import admin
from .models import Article


# Register your models here.

class Asettings(admin.ModelAdmin):
    list_display=['title','author','adate','udate']
    ordering=['title']
    search_fields=['title']
    list_display_links = ['title']




admin.site.register(Article,Asettings)










