from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from server import forms

@csrf_exempt
@login_required
def addProductivityRecord(request):
    if (request.method == "POST"):
        JSONdict = json.loads(request.body)
        print(JSONdict)

        if not JSONdict.get("time_start") or not JSONdict.get("time_end") or not JSONdict.get("time_productive"):
            return HttpResponse("No time_start or time_end or time_productive")


        try:
            data = {"time_start":JSONdict.get("time_start"),
                    "time_end":JSONdict.get("time_end"),
                    "time_productive":JSONdict.get("time_productive")}

            user_record = forms.UserRecordForm(data=data).save(commit=False)
            user_record.user_profile = request.user.user_profile
            user_record.save()

            return HttpResponse("Success!")
        except Exception as e:
            print(e)

        return HttpResponse("Failure :(")




