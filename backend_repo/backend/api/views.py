from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class Tik(APIView):

    def get(self, request):
        url = "http://rand:6000/tik/"

        payload = {}
        headers = {}

        response = requests.get(url, headers=headers, data=payload)

        if response.status_code == 200:
            return Response({"tik": "tik"})
        return Response({"message": "Hello, world!"})
