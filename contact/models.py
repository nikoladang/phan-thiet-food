from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    title = models.CharField(max_length=120, blank=True, null=True)
    message = models.CharField(max_length=120, blank=True, null=True)
    timestamp =  models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.full_name