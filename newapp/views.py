from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def current(request):
    response = HttpResponse()
    return render(request, 'newapp/6txtformat.html')


def lthree(request):
    response = HttpResponse()
    return render(request, 'newapp/3with_body.html')


def lfour(request):
    response = HttpResponse()
    return render(request, 'newapp/4hiding.html')

# def lesson(request):
#     response = HttpResponse()
#     return render(request, 'newapp/homepage.html')
#
# def lesson(request):
#     response = HttpResponse()
#     return render(request, 'newapp/homepage.html')
