from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from server import forms


def user_register(request):
    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.ProfileForm()

    return render(request, 'server/registration/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@csrf_exempt
def user_login(request):

    if(request.user.is_authenticated):
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                print(user)
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "server/registration/login.html", {"error": "Account deactivated!!"})
        else:
            return render(request, "server/registration/login.html", {"error": "Incorrect username or password!!"})

    return render(request, 'server/registration/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

