import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server import models

def index(request):
    return render(request, "server/base/index.html", {})

@login_required
def profile(request, user_id):

    user_profile = models.UserProfile.objects.get(user_id=user_id)

    if(user_profile):
        user_records = models.UserRecord.objects.filter(user_profile=user_profile).order_by("-time_start")

        productivity_data = []
        emotion_data = []
        for record in user_records:
            if((record.time_end - record.time_start) != 0):
                percentage = record.time_productive/(record.time_end - record.time_start) * 100
            else:
                percentage = 0

            productivity_data.append({"date":str(record.time_start.strftime("%Y-%m-%d %H:%M")), "productivity":str(percentage)})



            emote_dict = json.loads(record.emotion_data)

            for key, value in emote_dict.items():
                emote_dict[key] = '{0:.3f}'.format(float(value) * 100)
            emote_dict["date"] = str(record.time_start.strftime("%Y-%m-%d %H:%M"))
            emotion_data.append(emote_dict)


        print(emotion_data)

    return render(request, "server/base/profile.html", {"user_id":user_id,
                                                        "productivity_data":json.dumps(productivity_data),
                                                        "emotion_data":json.dumps(emotion_data)})
