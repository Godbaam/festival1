from django.db import models
from django.conf import settings
# Create your models here.

class Lostfound(models.Model):
    
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('작성 일시')
    image = models.ImageField(blank = True, upload_to='images/')
    body = models.TextField()
    where = models.CharField(max_length=200)
    
    def __str__(self): 
        return self.title

    def summary(self): 
        return self.body[:100]

class Comment(models.Model):
    lostfound=models.ForeignKey('Lostfound',on_delete=models.CASCADE, related_name='comments')
    nickname=models.CharField(max_length=100)
    text=models.TextField()

    def __str__(self):
        return self.text
    


