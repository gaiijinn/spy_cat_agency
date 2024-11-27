from rest_framework import viewsets
from . import serializers
from cats.models import Cat


# Create your views here.


class CatsModelViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('-id')
    serializer_class = serializers.CatSerializer
