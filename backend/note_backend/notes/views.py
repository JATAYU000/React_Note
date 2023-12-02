from django.shortcuts import render
# from rest_framework.views import APIView
from .serializers import NoteSerializer
from .models import Note
# from rest_framework.response import Response

# # Create your views here.

# class NoteView(APIView):
#     def get(self,request):
#         output=[{'title':output.title, 
#                  'description':output.description, 
#                  'dueDate': output.dueDate}
#                  for output in Note.objects.all()]
#         return Response(output)
    
#     def post(self,request):

#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        


from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
    permission_classes = (IsAuthenticated, )   
    def get(self, request):       
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}   
        return Response(content)
    

    
# class NoteView(generics.ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer