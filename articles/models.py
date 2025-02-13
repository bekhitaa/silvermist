from django.db import models

# Create your models here.
class Article(models.Model):
    title= models.CharField(max_length=40)
    author= models.CharField(max_length=40)
    content= models.TextField(max_length=1000)
    adate= models.DateTimeField(auto_now=False,auto_now_add=True)
    udate= models.DateTimeField(auto_now_add=False,auto_now=True)


    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']



