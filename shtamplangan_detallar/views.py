from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ProductSerializers, GalerySerializers, ProductSerializers2
from .models import ProductModel, GaleryModel
from rest_framework import generics


# Create your views here.
class sa(generics.CreateAPIView):
    parser_class = [MultiPartParser, FormParser]
    serializer_class = ProductSerializers


class s1a(generics.CreateAPIView):
    queryset = GaleryModel.objects.all()
    serializer_class = GalerySerializers

class s2a(generics.ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers2
