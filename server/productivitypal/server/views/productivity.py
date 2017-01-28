from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def update(request):
    if(request.method == "POST"):
        print(json.loads(request.body))
        return HttpResponse(request.POST)
