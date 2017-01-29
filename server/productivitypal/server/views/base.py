import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from server import models

def index(request):
    return render(request, "server/base/index.html", {})

@login_required
def profile(request, user_id):

    user = models.UserProfile.get(user__id=user_id)

    if(user):
        user_records = models.UserRecords.objects.filter(user_profile=user.user_profile, order_by="-time_start")

        print(user_records)
        productivity_data = []



    return render(request, "server/base/profile.html", {"user_id":user_id,
                                                        "productivity_data":json.dumps(productivity_data)})
