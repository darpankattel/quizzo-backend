from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class QuizCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.JSONField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quiz Categories"
        ordering = ['-id']


class QuizLevel(models.Model):

    QUIZ_LEVEL_NUMBER = {
        'Novice': '1',
        'Adept': '2',
        'Elite': '3',
        'Mastermind': '4',
    }
    level = models.CharField(max_length=255)
    xpfactor = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(1)])

    def __str__(self):
        return f"{self.QUIZ_LEVEL_NUMBER[self.level]}. {self.level}"

    @property
    def level_no(self):
        return self.QUIZ_LEVEL_NUMBER[self.level]

    class Meta:
        verbose_name_plural = "Quiz Levels"
        ordering = ['-id']


class Quiz(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    level = models.ForeignKey(QuizLevel, on_delete=models.CASCADE)
    qsn = models.TextField()
    options = models.JSONField()
    correct_index = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)])

    def __str__(self):
        return f"{self.category.name} - {self.qsn[:50]}"

    @property
    def correct_option(self):
        return self.options[self.correct_index]

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['-id']
