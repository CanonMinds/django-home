# from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def get_queryset(self):
        return self.queryset.filter(task_id=self.kwargs.get('task_pk'))#Learn how to use PK

    def perform_create(self, serializer):
        task = get_object_or_404(models.Task, pk=self.kwargs.get('task_pk'))
        serializer.save(task=task)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(),
            task_id=self.kwargs.get('task_pk'),
            pk=self.kwargs.get('pk'))


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        self.pagination_class.page_size = 2
        reviews = models.Review.objects.filter(task_id=pk)

        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = serializers.ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializer.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

