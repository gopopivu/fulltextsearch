from django.db import models

class SearchResult(models.Model):
  filename = models.CharField(max_length=255, unique=True)
  url = models.URLField(max_length=2000)
  html = models.TextField()
  normalized_html = models.TextField(default='')
  title=models.CharField(max_length=255, default='')

