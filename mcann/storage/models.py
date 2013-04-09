from django.db import models
from django.contrib.auth import models as authmodel
from django.utils import timezone

class Anndata(models.Model):
    user = models.ForeignKey(authmodel.User)
    permissions = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    ranges = models.CharField(max_length=200)
    quote = models.CharField(max_length=200)
    uri = models.CharField(max_length=200)