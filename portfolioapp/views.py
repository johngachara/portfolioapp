from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,template_name='home.html')
def about(request):
    return render(request,template_name='about.html')
def projects(request):
    return render(request,'projects.html')
def contact(request):
    return render(request,'contact.html')
