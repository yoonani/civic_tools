from django.db import models

import datetime
from django.utils import timezone


# Create your models here.

class Contents(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    def was_published_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)
    def __str__(self):
        return self.title
