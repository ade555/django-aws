from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status

from django.shortcuts import get_object_or_404

from . import models
from . import serializers


class TaskListCreate(generics.GenericAPIView):
    serializer_class = serializers.TaskSerializer

    def get(self, request:Request):
        data = models.Task.objects.all()

        serializer = self.serializer_class(instance=data, many=True)
        response = {
                "message":"successful",
                "data":serializer.data
            }
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

class TaskRetrieveUpdateDelete(generics.GenericAPIView):
    serializer_class = serializers.TaskSerializer

    def get(self, request:Request, task_id:int):
        task = get_object_or_404(models.Task, id=task_id)

        serializer = self.serializer_class(instance=task)
        response = {
                "message":"successful",
                "data":serializer.data
            }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def put(self, request:Request, task_id:int):
        task = get_object_or_404(models.Task, id=task_id)

        serializer = self.serializer_class(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, task_id:int):
        task = get_object_or_404(models.Task, id=task_id)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)