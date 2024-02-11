from django.urls import path, include
from rest_framework.views import APIView
from core.response import MyResponse

class IndexView(APIView):
    def get(self, request, format=None):
        return MyResponse.success(message="Hurraaayyy, active!")

urlpatterns = [
    path('', IndexView.as_view()),
    path('quiz/', include('quiz.urls')),
    path('acc/', include('account.urls')),
    path('record/', include('record.urls')),
]
