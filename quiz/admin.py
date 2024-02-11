from django.contrib import admin
from .models import QuizCategory, QuizLevel, Quiz

admin.site.register(QuizCategory)
admin.site.register(QuizLevel)
admin.site.register(Quiz)

