from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('faculty', 'Faculty'),
        ('core', 'Core Member'),
        ('oc', 'Organizing Committee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
