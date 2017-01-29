import os

import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE','productivitypal.settings')

import django
django.setup()

import data as emotion_data
import datetime

import random

from django.contrib.auth.models import User

from server.models import UserProfile, UserRecord


def populate():

    user = add_user({"username":"test", "password":"banana12345"})

    for i in range(0,7):
        data = {"time_start": datetime.datetime.now() - datetime.timedelta(0,(i+1)*3600),
                "time_end": datetime.datetime.now() - datetime.timedelta(0, i*3600),
                "time_productive": datetime.timedelta(0, random.randint(0,3600)),
                "emotion_data":json.dumps(emotion_data.emotion_data[i])}

        add_record(user, data)



def add_record(user_profile, data):

    user_record, created = UserRecord.objects.get_or_create(time_start=data["time_start"],
                                                            time_end=data["time_end"],
                                                            time_productive=data["time_productive"],
                                                            user_profile=user_profile,
                                                            emotion_data=data["emotion_data"])
    user_record.save()

    return user_record



def add_user(data):
    u, created = User.objects.get_or_create(username=data["username"])

    u.set_password(data["password"])
    u.save()

    d, created = UserProfile.objects.get_or_create(user=u)
    d.save()

    return d



if __name__ == "__main__":
    populate()