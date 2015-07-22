from django import forms
from .models import ReviewRequest


class ReviewRequestForm(forms.ModelForm):
    class Meta:
        model = ReviewRequest
        fields = ['github_repo', 'info', 'create_issue']
