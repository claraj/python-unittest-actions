from django.shortcuts import render, HttpResponse
from .math import addition


def hello(request):
    """
    This view handles the home page request.
    It returns a friendly greeting message to the user.
    """
    return HttpResponse('Hello everyone!')


def two_plus_two(request):
    total = addition(2, 2)
    return HttpResponse(f'Two plus two is {total}')
