from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='records')
    result_choices = [
        ('right', 'Right'),
        ('wrong', 'Wrong'),
        ('skipped', 'Skipped'),
    ]
    result = models.CharField(max_length=10, choices=result_choices)

    class Meta:
        unique_together = ['user', 'quiz']
        ordering = ['-id']

    def __str__(self):
        return f"{self.user.username} - {self.quiz} - {self.result}"
