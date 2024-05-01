from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from core.response import MyResponse
from core.pagination import CustomPagination
from .models import Quiz, QuizCategory, QuizLevel
from .serializers import QuizCategorySerializer, QuizQuestionSerializer, QuizAnswerSerializer
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from record.models import Record
from record.serializers import RecordWriteSerializer
from core.utils import convert_null_to_none
import random


class QuizView(APIView):
    """
    Get the details of the quiz, without the answer
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        level_name = request.GET.get('level_name')
        category_id, level_name = convert_null_to_none(category_id, level_name)

        quiz = Quiz.objects.all()
        if category_id:
            quiz = quiz.filter(category__id=category_id)
        if level_name:
            quiz = quiz.filter(level__level__icontains=level_name)
        quiz = quiz.exclude(records__user=request.user).first()
        # TODO: Add Machine Learning here
        if not quiz:
            return MyResponse.failure(message="Quiz not found", status_code=status.HTTP_404_NOT_FOUND)
        serializer = QuizQuestionSerializer(quiz)
        return MyResponse.success(data=serializer.data)


class QuizAnswerView(APIView):
    """
    Check the answer and record the result

    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id, *args, **kwargs):
        if Quiz.objects.filter(id=quiz_id).exists():
            quiz = Quiz.objects.get(id=quiz_id)
            answer = request.GET.get('answer')
            answer = convert_null_to_none(answer)
            is_correct = False
            if answer:
                if quiz.correct_index == int(answer):
                    result = "right"
                    is_correct = True
                else:
                    result = "wrong"
            else:
                result = "skipped"
            record = {"user": request.user.id,
                      "quiz": quiz.id, "result": result}
            record_serializer = RecordWriteSerializer(data=record)
            if record_serializer.is_valid(raise_exception=True):
                record_serializer.save()
            serializer = QuizAnswerSerializer(quiz)
            return MyResponse.success(data={**serializer.data, "is_correct": is_correct})
        return MyResponse.failure(message="Answer not found", status_code=status.HTTP_404_NOT_FOUND)


class CategoryListView(ListAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer
    pagination_class = CustomPagination


class CategoryListAllView(ListAPIView):
    queryset = QuizCategory.objects.all()
    serializer_class = QuizCategorySerializer


class ScriptView(APIView):
    def get(self, request, *args, **kwargs):
        # quizzes = []
        # for i in range(17):
        #     for j in range(30):
        #         print(i, j)
        #         quizzes.append(
        #             {
        #                 "category": QuizCategory.objects.get(id=i + 1),
        #                 "level": QuizLevel.objects.get(id=random.randint(1, 4)),
        #                 "qsn": f"Question ({i + 1}, {j + 1 + 30})?",
        #                 "options": [
        #                     "Opt 1",
        #                     "Opt 2",
        #                     "Opt 3",
        #                     "Opt 4"
        #                 ],
        #                 "correct_index": random.randint(0, 3)
        #             }
        #         )

        # for quiz in quizzes:
        #     Quiz.objects.create(**quiz)
        return MyResponse.success(data="", message="Successfully added")
