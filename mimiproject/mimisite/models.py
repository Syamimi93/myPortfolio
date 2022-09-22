from django.db import models

class Members(models.Model):
    
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

class ContactForm(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
