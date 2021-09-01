from django.urls import path

from api.views import FooDetail, FooList

urlpatterns = [

    path('foo/', FooList.as_view()),
    path('foo/<int:pk>/', FooDetail.as_view()),


]
