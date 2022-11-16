from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tutorials.models import tutorial
from tutorials.serializer import TutorialSerializer
from django.shortcuts import get_object_or_404, render
from django.core import serializers

class ListCreateTutorialView(ListCreateAPIView):
    model= tutorial
    serializer_class= TutorialSerializer
    def get_queryset(self):
        SomeModel_json=  tutorial.objects.all()
        return JsonResponse(SomeModel_json) 
    def create(self, request, *args, **kwargs):
        serializer= TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Tutorial successfull'
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'message': 'Create a new Tutorial unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteTutorialView(RetrieveUpdateDestroyAPIView):
    model= tutorial
    serializer_class= TutorialSerializer

    def put(self, request, *args, **kwargs):
        tutorial= get_object_or_404(tutorial, id=kwargs.get('pk'))
        serializer= TutorialSerializer(tutorial,data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                    'message': 'update a new Tutorial successfull'
                }, status=status.HTTP_200_OK)
        return JsonResponse({
            'message': 'update a new Tutorial unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        tutorial= get_object_or_404(tutorial, id=kwargs.get('pk'))
        tutorial.delete()
        return JsonResponse({
                    'message': 'delete a new Tutorial successfull'
                }, status=status.HTTP_200_OK)




        