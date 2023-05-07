from django.db import models
from django.db import models

class Booking(models.Model):
    artist = models.CharField(max_length=255)
    date = models.DateField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} - {self.artist} - {self.date}'
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
