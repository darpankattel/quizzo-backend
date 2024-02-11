from rest_framework.views import APIView
from core.response import MyResponse

class MockView(APIView):
    def get(self, request, *args, **kwargs):
        return MyResponse.success()