from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sharedpicture(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_pictures')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_pictures')
    picture = models.ImageField(upload_to='image_storage/')
    time_of_transfer = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shared Picture from {self.sender} to {self.receiver} at {self.time_of_transfer}"