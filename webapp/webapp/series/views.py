import logging

from rest_framework import generics

from .import models
from .import serializers

logging.basicConfig()
log = logging.getLogger(__name__)


class Series(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.SeriesSerializer
    queryset = models.Series.objects
