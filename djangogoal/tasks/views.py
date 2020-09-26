# from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from . import models
from . import serializers

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class ListCreateTask(APIView):
#     def get(self, request, format=None):
#         tasks = models.Task.objects.all()
#         serializer = serializers.TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = serializers.TaskSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListCreateTask(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer 

class RetrieveUpdateDestroyTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer