# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer

''' Basic Usage Of Django Rest Framework'''
@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, snippet_id):
#     try:
#         snippet = Snippet.objects.get(id=snippet_id)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''Using APIView'''
class SnippetDetail(APIView):
    def get_object(self, snippet_id):
        try:
            return Snippet.objects.get(id=snippet_id)
        except Snippet.DoesNotExist:
            raise Http404
    def get(self, request, snippet_id, format=None):
        snippet = self.get_object(snippet_id=snippet_id)
        serializer = SnippetSerializer(snippet)
        return Response(data=serializer.data)
    def put(self, request, snippet_id, format=None):
        snippet = self.get_object(snippet_id=snippet_id)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, snippet_id, format=None):
        snippet = self.get_object(snippet_id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
