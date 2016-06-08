from django.db import models

class SearchResult(models.Model):
  filename = models.CharField(max_length=255)
  url = models.CharField(max_length=2000)
  html = models.TextField()

