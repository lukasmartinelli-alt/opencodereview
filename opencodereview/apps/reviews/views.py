from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from github3 import login

def home(request):

    user = request.user
    if user and user.is_authenticated():
        auth = user.social_auth.get(provider='github')
        gh = login(token=auth.access_token)

    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def browse(request):
    return render(request, 'browse.html')

def new(request):
    return render(request, 'new.html')
