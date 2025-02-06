from django.contrib import admin
from .models import NewsCategory, News, Favorite

# Register your models here.
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(Favorite)
