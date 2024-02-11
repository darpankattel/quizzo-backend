from rest_framework import serializers
from .models import Record


class RecordWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["user", "quiz", "result"]


class RecordReadSerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField()
    xp = serializers.FloatField()

    class Meta:
        model = Record
        fields = ["quiz", "result", "xp"]
