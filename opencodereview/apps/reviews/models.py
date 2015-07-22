from django.db import models
from django.contrib.auth.models import User

PENDING = 0
REVIEWED = 1
STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (REVIEWED, 'Reviewed'),
)


class ReviewRequest(models.Model):
    submitter = models.ForeignKey(User)
    github_repo = models.CharField(max_length=250)
    info = models.TextField()
    create_issue = models.BooleanField(default=False)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)


class Review(models.Model):
    request = models.ForeignKey(ReviewRequest)
    reviewer = models.ForeignKey(User)
    info = models.TextField()
