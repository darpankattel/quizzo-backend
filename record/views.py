from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from core.response import MyResponse
from core.pagination import CustomPagination
from .serializers import RecordReadSerializer
from knox.auth import TokenAuthentication
from .models import Record
from django.db.models import F, Sum
from .utils import transform_to_level
from quiz.models import Quiz
from constants import MAXIMUM_USER_LEVEL, XP_FACTOR_MULTIPLIER
from django.db.models import Q


class RecordView(ListAPIView):
    serializer_class = RecordReadSerializer
    pagination_class = CustomPagination
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        records = Record.objects.filter(user=self.request.user)
        # for each record, get the quiz__level__xpfactor
        records = records.annotate(
            xp=F('quiz__level__xpfactor') * XP_FACTOR_MULTIPLIER)
        return records


class RecordProfileView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        user_total_xp = Record.objects.filter(user=user).aggregate(
            total_xp=Sum('quiz__level__xpfactor'))['total_xp']
        user_level = transform_to_level(user_total_xp) * MAXIMUM_USER_LEVEL
        total_quizzes = Quiz.objects.filter(records__user=user).count()
        total_right_quizzes = Quiz.objects.filter(
            Q(records__user=user) & Q(records__result='right')).count()
        return MyResponse.success(data={
            'user_total_xp': user_total_xp,
            'user_level': user_level,
            'total_quizzes': total_quizzes,
            'total_right_quizzes': total_right_quizzes
        })
