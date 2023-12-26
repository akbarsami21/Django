from django.shortcuts import render
from django.http import HttpResponse
from . form import TeacherForm

# Create your views here.
def blog(request):
    return HttpResponse("this is blog page")

def blog1(request):
    return HttpResponse("this is blog1 page")

def blog2(request):
    return HttpResponse("this is blog2 page")
