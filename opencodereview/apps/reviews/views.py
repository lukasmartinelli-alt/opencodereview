from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from github3 import login

from .forms import ReviewRequestForm

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
    if request.method == 'POST':
        form = ReviewRequestForm(request.POST)

        if form.is_valid():
            review_request = form.save(commit=False)
            review_request.submitter = request.user
            review_request.save()

            return redirect('/')

        return render(request, 'new.html', {
            'form': form     
        })
    else:
        form = ReviewRequestForm()
        return render(request, 'new.html', {
            'form': form     
        })
