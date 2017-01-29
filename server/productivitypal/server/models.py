from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)


# Represents some interval of time that the user is working
# Allows historical searching of user data
class UserRecord(models.Model):
    user_profile = models.ForeignKey("UserProfile")
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()


# An interval of time and an associated interval of productive time
class ProductivityInterval(models.Model):
    time_productive = models.DurationField()
    time_total = models.DurationField()


#Represents time spent productively browsing done over a productivity interval
class WindowInterval(models.Model):
    user_record = models.ForeignKey("UserRecord")
    productivity_interval = models.ForeignKey("ProductivityInterval")












#Represents a git repository
class Repository(models.Model):
    url = models.CharField(max_length=200, unique=True)
    contributors = models.ManyToManyField("UserProfile")


#Represents work done on a repository over a productivity interval
class RepositoryInterval(models.Model):
    repository = models.ForeignKey("Repository")
    lines = models.IntegerField()
    words = models.IntegerField()
    productivity_interval = models.ForeignKey("ProductivityInterval")