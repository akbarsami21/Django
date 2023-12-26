from django.shortcuts import render
from . forms import TeacherForm
# Create your views here.
def teacherform(request):
    if request.method== 'POST':
        fm=TeacherForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
        

    else:
        fm=TeacherForm()
        print(fm)
        print('this is get form')
        
       
    
    return render(request,'blogs/tform.html',{'form':fm})