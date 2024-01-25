from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello, world! Wellcome to the Loop\'n\'pooL project.')
