from concurrent.futures import ThreadPoolExecutor

from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from github3 import login

from .forms import ReviewRequestForm
from .models import ReviewRequest


def _authenticate_github_api(request):
    user = request.user
    if user and user.is_authenticated():
        auth = user.social_auth.get(provider='github')
        return login(token=auth.access_token)

    return login(token=APP_AUTH_TOKEN)

def home(request):
    gh = _authenticate_github_api(request)
    review_requests = ReviewRequest.objects.all()
    repos = []

    """
    def repo_detail(repo):
        full_repo = gh.repo(repo)
        repos.append(full_repo) # Is only save because of GIL!

    with ThreadPoolExecutor(max_workers=10) as thread_pool:
        for review_request in review_requests:
            thread_pool.submit(repo_detail, review_request.github_repo)
        
    """
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
