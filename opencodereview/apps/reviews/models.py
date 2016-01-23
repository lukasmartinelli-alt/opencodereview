from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

PENDING = 0
REVIEWED = 1
STATUS_CHOICES = (
    (PENDING, 'Pending'),
    (REVIEWED, 'Reviewed'),
)


class ReviewRequest(models.Model):
    submitter = models.ForeignKey(User)
    review_info = models.TextField()
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    repo_owner = models.TextField()
    repo_name = models.TextField()
    repo_avatar_url = models.URLField()
    repo_description = models.TextField()
    repo_stars = models.IntegerField(default=0)

    def repo_full_name(self):
        return '{}/{}'.format(self.repo_owner, self.repo_name)


class Review(models.Model):
    request = models.ForeignKey(ReviewRequest)
    reviewer = models.ForeignKey(User)
    info = models.TextField()
