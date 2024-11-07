from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def welcome(request):
#     return HttpResponse("Welcome and Helooo from Django")


# def about(request):
#     return HttpResponse("Hi I am Django Developer!")

def empty(request):
    return HttpResponse(f"Empty Url")


def id_index(request, input):
    return HttpResponse(f"entered id is {input}")


def index(request, input):
    displayed_text = None
    if input == "welcome":
        displayed_text = "Welcome and Helooo from Django"
    elif input == "about":
        displayed_text = "Hi, I am Django Developer!"
    else:
        return HttpResponseNotFound("Not A Valid Entry")
    return HttpResponse(displayed_text)
