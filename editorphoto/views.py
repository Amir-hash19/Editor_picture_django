from django.shortcuts import render
from django.http.response import HttpResponse




def editor_page(request):
    return HttpResponse("this is editor page")
