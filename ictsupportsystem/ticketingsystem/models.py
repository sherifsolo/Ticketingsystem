from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Users(AbstractUser):
    username = models.CharField(max_length=255, unique=True, default='stafflabour')
    phonenumber = models.IntegerField(blank=True, null=True, default=None)
    email = models.EmailField(unique=True, blank=False, default='labour@mail.govmail.ke')
    role = models.CharField(max_length=64, default='staff')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phonenumber', 'email']

    def __str__(self):
        return f"user: {self.username} | role: {self.role}"


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('resolved', 'Resolved'),
        ('escalated', 'Escalated'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    tId = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=64)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='low')
    uploads = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    agent = models.CharField(max_length=200)
    creationDateTime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket ID: {self.tId} | Title: {self.title} | Owner: {self.owner}"