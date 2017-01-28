import json
from django.shortcuts import render


def index(request):
    return render(request, "server/base/index.html", {})

def profile(request, user_id):
    productivity_data = [
                          {"date":"0",
                           "productivity":"25"},
                          {"date": "0",
                           "productivity": "25"},
                          {"date": "1",
                           "productivity": "50"},
                          {"date": "2",
                           "productivity": "43"},
                          {"date": "3",
                           "productivity": "10"},
                          {"date": "4",
                           "productivity": "3"}]
    return render(request, "server/base/profile.html", {"user_id":user_id,
                                                        "productivity_data":json.dumps(productivity_data)})
