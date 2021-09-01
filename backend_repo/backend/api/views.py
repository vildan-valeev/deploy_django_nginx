from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Foo
from api.serializers import FooSerializer


def main_page(request):
    return render(request, "main.html")


class FooList(ListCreateAPIView):
    serializer_class = FooSerializer
    queryset = Foo.objects.all()


class FooDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = FooSerializer
    queryset = Foo.objects.all()
