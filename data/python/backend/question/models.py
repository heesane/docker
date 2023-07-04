from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    