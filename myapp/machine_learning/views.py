from django.http import HttpResponse
# Create your views here.
def machine(request):
    sum=25+2
    return HttpResponse(f"<h2>Welcome To Our Website {sum}</h2>")

def about(request):
    sum=25+2
    return HttpResponse("this is about section")
