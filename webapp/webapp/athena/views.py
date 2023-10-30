from rest_framework import generics, status
from rest_framework.response import Response


class HealthCheck(generics.GenericAPIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        response = {
            'status': 200,
        }
        return Response(response, status=status.HTTP_200_OK)
