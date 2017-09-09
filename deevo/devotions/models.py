import datetime

from django.contrib.auth.models import User
from django.db import models

class Devotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    verse_start = models.IntegerField()
    verse_end = models.IntegerField(null=True, blank=True)
    version_id = models.IntegerField()
    reflection = models.TextField()
    pub_date = models.DateTimeField()
    edit_date = models.DateTimeField(null=True, blank=True)