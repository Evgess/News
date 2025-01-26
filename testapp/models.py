from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    category_title = models.CharField(max_length=128)
    category_text = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)


