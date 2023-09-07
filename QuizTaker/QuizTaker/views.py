from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request=request,template_name='QuizTaker/home.html')