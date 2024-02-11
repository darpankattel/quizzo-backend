from rest_framework import serializers
from .models import QuizCategory, Quiz
class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        exclude = ('keywords',)

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "category", "level", "qsn", "options"]

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ["id", "correct_index", "correct_option"]