from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json


@login_required
def addProductivityRecord(request):
    if (request.method == "POST"):
        JSONdict = json.loads(request.body)
        print(JSONdict)