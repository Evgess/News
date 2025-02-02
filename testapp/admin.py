from django.contrib import admin
from .models import NewsCategory, News, Card

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(Card)
