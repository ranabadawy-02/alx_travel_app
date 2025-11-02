from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestView(APIView):
    """
    A simple test endpoint.
    """
    def get(self, request):
        return Response({"message": "ALX Travel API is working!"}, status=status.HTTP_200_OK)
