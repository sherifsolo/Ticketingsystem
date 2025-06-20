from django.db import models

# Create your models here.
class Ticket(models.Model):
  statusChoices = [
    ('open', 'Open'),
    ('resolved', 'Resolved'),
    ('escalated', 'Escalated'),
  ]
  priorityLevelChoices = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
  ]
  tId = models.CharField(max_length=64)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  category = models.CharField(max_length=64)
  priority = models.CharField(max_length=15, choices= priorityLevelChoices, default='low')
  uploads = models.CharField(max_length=255)
  status = models.CharField(max_length=20, choices=statusChoices, default='open')
  agent = models.CharField(max_length=200)
  creationDateTime = models.DateTimeField(auto_now_add=True)
  #column to link ticket to user

  def __str__(self):
    return f"id:{self.tId} title:{self.title} \ndescription:{self.description} \ncategory:{self.category} \npriority:{self.priority} \nuploads:{self.uploads} \n"
  

  class Users(models.Model):
    name = models.CharField(max_length=255, blank=False)
    password = models.TextField(blank=False)
    role = models.CharField(max_length=64, default='staff')


    def __str__(self):
      return f"user : {self.name}  role: {self.role}"

