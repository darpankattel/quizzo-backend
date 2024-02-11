from django.db import models
from django.contrib.auth.models import User
from quiz.models import QuizCategory

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    interested_in = models.ManyToManyField(QuizCategory, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'