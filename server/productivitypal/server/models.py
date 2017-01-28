from django.db import models

# Create your models here.

def UserProfile(models.Model):
    user = OneToOneField("User")
    productivityRating = IntegerField()

