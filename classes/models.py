from django.db import models

from django.db import models
from django.contrib.auth.models import User

class DanceClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    level = models.CharField(max_length=50)
    max_participants = models.IntegerField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dance_class = models.ForeignKey(DanceClass, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.dance_class.title}"