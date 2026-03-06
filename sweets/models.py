from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=12) 
    desc = models.TextField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.name