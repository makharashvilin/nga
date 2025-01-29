from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField()
    edited = models.BooleanField()
    write_date = models.DateTimeField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, related_name='posts')


class Category(models.Model):
    name = models.CharField(max_length=100)
