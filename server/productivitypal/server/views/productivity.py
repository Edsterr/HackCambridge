from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update(request):
    if(request.method == "POST"):
        print(json.loads(request.body))
        return HttpResponse(request.POST)
import json

from server import forms

@login_required
def addProductivityRecord(request):
    if (request.method == "POST"):
        JSONdict = json.loads(request.body)
        print(JSONdict)

        if not JSONdict.get("time_start") or not JSONdict.get("time_end"):
            return HttpResponse("No time_start or time_end")

        data = {"time_start":JSONdict.get("time_start"),
                "time_end":JSONdict.get("time_end")}

        user_record = forms.UserRecordForm(data).save(commit=False)
        user_record.user_profile = request.user.user_profile
        user_record.save()

        intervals = JSONdict.get("window_intervals")
        if intervals:
            for interval in intervals:
                window = forms.WindowIntervalForm().save(commit=False)rl
                
                data = {""}
