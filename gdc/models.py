from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    main_nav = models.BooleanField()
    url_key = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    """
    Symbolic links will actually link to a route and are simply for making navigation items for them dynamically
    """
    symbolic = models.TextField(default="no")

class News(models.Model):
    posted = models.DateTimeField(default=datetime.now())
    title = models.CharField(max_length=30)
    body = models.TextField()
    by = models.ForeignKey(User)