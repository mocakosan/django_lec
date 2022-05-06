from django.db import models

# Create your models here.
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    imgfile = models.ImageField(null=True, upload_to="media/", blank=True)

class Notices(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')