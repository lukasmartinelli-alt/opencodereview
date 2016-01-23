from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings

from github3 import login

from .forms import ReviewRequestForm
from .models import ReviewRequest


def _authenticate_github_api(request):
    user = request.user
    if user and user.is_authenticated():
        auth = user.social_auth.get(provider='github')
        return login(token=auth.access_token)

    return login(token=settings.SOCIAL_AUTH_GITHUB_SECRET)


def home(request):
    review_requests = ReviewRequest.objects.all()
    reviewers = User.objects.all()
    return render(request, 'home.html', {
        'requests': review_requests,
        'reviewers': reviewers
    })


def logout(request):
    auth_logout(request)
    return redirect('/')


def browse(request):
    review_requests = ReviewRequest.objects.all()
    return render(request, 'browse.html', {
        'requests': review_requests
    })


def update_review_request_from_github(gh, request_review):
    repo = gh.repository(request_review.repo_owner, request_review.repo_name)
    submitter = gh.user(request_review.submitter.username)
    request_review.repo_avatar_url = submitter.avatar_url
    request_review.repo_description = repo.description
    request_review.repo_stars = repo.stargazers
    return request_review


def new(request):
    if request.method == 'POST':
        form = ReviewRequestForm(request.POST)

        if form.is_valid():
            review_request = form.save(commit=False)
            review_request.submitter = request.user

            repo_owner, repo_name = form.cleaned_data['github_repo'].split('/')
            review_request.repo_owner = repo_owner
            review_request.repo_name = repo_name

            gh = _authenticate_github_api(request)
            update_review_request_from_github(gh, review_request)

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
