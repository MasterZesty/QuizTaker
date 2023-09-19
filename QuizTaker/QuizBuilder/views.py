from django.http import HttpResponse
from django.shortcuts import render


def quiz(request):
    #return HttpResponse("Hello, world. You're at the quiz.")
    return render(request=request,template_name='QuizBuilder/quiz.html')

def dashboard(request):
    #return HttpResponse("Hello, world. You're at the quiz.")
    return render(request=request,template_name='QuizBuilder/dashboard.html')