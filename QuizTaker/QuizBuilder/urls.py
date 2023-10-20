"""
URL configuration for QuizBuilder App.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'quizbuilder'

urlpatterns = [

    path("login/", views.login, name="quizbuilder_login"),
    path("logout/", views.logout, name="quizbuilder_logout"),
    path("signup/", views.signup, name="quizbuilder_signup"),


    path("home/", views.home, name="quizbuilder_home"),
    path("quizzes/", views.quizzes, name="quizbuilder_quizzes"),
    path("pricing/", views.pricing, name="quizbuilder_pricing"),
    path("about/", views.about, name="quizbuilder_about"),
    path("contact/", views.contact, name="quizbuilder_contact"),



    path("quiz/", views.quiz, name="quizbuilder_quiz"),
    path("dashboard/", views.dashboard, name="quizbuilder_dashboard"),
    path("create/", views.create_quiz, name="quizbuilder_create"),

]
