from django.shortcuts import render
from account.models import Teacher

# Create your views here.
def signup(request):
    return render(request,'account/signup.html')

def login(request):
    return render(request,'account/login.html')

def teacher_info(request):
    teacher= Teacher.objects.all()
    return render(request,'account/teacher.html',{'teach':teacher})
