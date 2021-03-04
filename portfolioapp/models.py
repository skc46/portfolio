from django.db import models

# Create your models here.

class ContactForm(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(blank=True)
    Message = models.TextField()

    def __str__(self):
        return self.Name
