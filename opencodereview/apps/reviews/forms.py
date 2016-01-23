from django import forms
from .models import ReviewRequest


class ReviewRequestForm(forms.ModelForm):
    github_repo = forms.CharField()

    class Meta:
        model = ReviewRequest
        fields = ['review_info']
