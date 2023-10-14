from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from .quiz_builder_api import api_create_quiz
from django.views.decorators.csrf import csrf_exempt


def quiz(request):
    #return HttpResponse("Hello, world. You"re at the quiz.")
    return render(request=request,template_name="QuizBuilder/take_quiz.html")

def dashboard(request):
    #return HttpResponse("Hello, world. You"re at the quiz.")
    return render(request=request,template_name="QuizBuilder/dashboard.html")

@csrf_exempt
def create_quiz(request):

    if request.method == "POST":
        
        try:
            data = json.loads(request.body.decode("utf-8"))

        except json.JSONDecodeError:
            response_data = {}
            response_data["status"] = "error"
            response_data["message"] = "please provide valid json"
            return JsonResponse(response_data)

        response_data = api_create_quiz(data, email='wdw@abc.com')

        return JsonResponse(response_data)

        return render(request=request,template_name="QuizBuilder/create_quiz.html",context=data)

    return render(request=request,template_name="QuizBuilder/create_quiz.html")