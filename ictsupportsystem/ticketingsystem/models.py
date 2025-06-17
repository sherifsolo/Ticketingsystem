from django.db import models

# Create your models here.
class Ticket(models.Model):
  tId = models.CharField(max_length=64)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  category = models.CharField(max_length=64)
  priority = models.CharField(max_length=15)
  uploads = models.CharField(max_length=255)
  status = models.CharField(max_length=20)
  agent = models.CharField(max_length=200)
  creationDateTime = models.DateTimeField()
  #column to link ticket to user