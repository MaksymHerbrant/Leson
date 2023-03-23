from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.models import STYLES_CHOICES, LANGUAGE_CHOICES

# Create your views here.
@csrf_exempt
def snippets_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

def styles_list(request):
    if request.method == "GET":
        return JsonResponse(STYLES_CHOICES, status=200, safe=False)
    
def language_list(request):
    if request.method == "GET":
        return JsonResponse(LANGUAGE_CHOICES, status=200, safe=False)