from django.db import models

# Create your models here.
class Tins(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(blank=True, null=True)
