from django.db import models
from django.utils import timezone  #import timezone

# Create your models here.

#Model for blogpost
class BlogPost(models.Model):
    title=models.CharField(max_length=60)
    text=models.TextField()
    created_date=models.DateField(default=timezone.now())  #set a default for datefield. Needed to prevent possible errors

#gives name for blog
    def __str__(self):
        return self.title