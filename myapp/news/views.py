from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def newstime(request):
    return render(request,"news/news.html")

def random(request):
    return render(request,"news/random.html")

def country(request):
    return render(request,"news/country.html")

def course(request):
    sclname="ifish school"
    cname="python basic to advanced"
    duration="3months"
    topic="variable,loops,function,oop, and so on."

    offering={'s':sclname,'c':cname,'d':duration,'t':topic}
    return render(request,"news/course.html",context=offering)

def teacher(request):
    teacher={'names':['sami','sakib','saikat','ruhul']}
    snames="sami"
    seat=40
    cd={"s":snames,"se":seat}
    combined_context = {**teacher, **cd}
    
    return render(request,'news/teacher.html',combined_context)

class DataAnalysis(View):
    def get(self,request):
        return render(request,'news/class.html')



