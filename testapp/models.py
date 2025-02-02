from django.db import models
from django.template.context_processors import media


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_name)


class News(models.Model):
    news_title = models.CharField(max_length=128)
    news_text = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    news_photo = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.news_title)


class Card(models.Model):
    user_id = models.IntegerField()
    user_news = models.ForeignKey(News, on_delete=models.CASCADE)
    user_news_count = models.IntegerField()

    def __str__(self):
        return str(self.user_id)


