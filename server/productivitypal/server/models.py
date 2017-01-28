from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField("User")


class ProductivityInterval(models.Model):
    user_profile = models.ForeignKey("UserProfile")
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()


class Repository(models.Model):
    url = models.CharField(unique=True)
    contributors = models.ManyToManyField("UserProfile")

class RepositoryInterval:
    productivity_interval = models.ForeignKey("ProductivityInterval")
    repository = models.ForeignKey("Repository")
    lines = models.IntegerField()
    words = models.IntegerField()


class BrowsingInterval(models.Model):
    productivity_interval = models.ForeignKey("ProductivityInterval")
    #Productive time spent browsing
    time_productivity = models.DurationField()