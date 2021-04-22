from django.db import models

class News(models.Model):
    title = models.CharField('Title', max_length=50)
    news = models.TextField('News')
    imgURL = models.CharField('URL', max_length=100)
