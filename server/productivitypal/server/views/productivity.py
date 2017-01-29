from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
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
        user_record.user = request.user
        user_record.save()

        intervals = JSONdict.get("window_intervals")
        if intervals:
            for interval in intervals:



