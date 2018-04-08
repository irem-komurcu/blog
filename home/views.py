from django.shortcuts import render,HttpResponse

# Create your views here.

"""def home_view(request):
    return HttpResponse('<b>Welcome</b>')"""

def home_view(request):
    if request.user.is_authenticated():
        context={
            'isim':'Irem',
        }
    else:
        context={
            'isim':'misafir',
        }

    return render(request,'home.html',context)

def about_view(request):
    return render(request,'about.html')

