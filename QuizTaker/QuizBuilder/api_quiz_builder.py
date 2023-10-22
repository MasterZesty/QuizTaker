
from .models import User, Quiz, QuizQuestion
from uuid import uuid4
from typing import Dict

def api_create_quiz(data, email):
    '''
    take raw json from frontend and make quiz
    from it then store it in bakend/db
    '''
    print(data)
    quiz_title = "not available"
    quiz_id = uuid4()
    user_id = api_get_user_id(email)

    for d in data:
        print(d)

        if d.get("heading","") != "":
            quiz_title = d.get("heading", "NA")
            try:
                quiz = Quiz(user_id=user_id, quiz_id=quiz_id, quiz_title=quiz_title)
                quiz.save()
            except Exception as e:
                response_data = {"status": "failure", "message": str(e)}
                return response_data

        if d.get("question","") != "":
            question_id = uuid4()
            question = d.get("question", "NA")
            option_a = d["options"].get("A","NA")
            option_b = d["options"].get("B","NA")
            option_c = d["options"].get("C","NA")
            option_d = d["options"].get("D","NA")
            correct_answer = d["options"].get("correct_answer","NA")

            try:
                question = QuizQuestion(quiz_id=quiz, question_id=question_id, question=question, option_a=option_a, option_b=option_b, option_c=option_c, option_d=option_d, correct_answer=correct_answer)
                question.save()
            except Exception as e:
                response_data = {"status": "failure", "message": str(e)}
                return response_data
        
    response_data = {}
    response_data["status"] = "success"
    response_data["message"] = "quiz created successfully"

    return response_data


def api_get_user_id(email):
    '''
    get user_id using email
    '''
    user_id = User.objects.get(email=email)
    return user_id


def api_create_user(user_details: Dict[str, str]):
    '''
    create user in db
    '''
    email = user_details.get('email','')
    name = user_details.get('name','')
    password = user_details.get('password','')

    if email != '' and name != '':
        try:
            user = User(email=email, name= name, password=password)
            user.save()

        except Exception as e:
            response_data = {"status": "failure", "message": str(e)}
            return response_data

        response_data = {}
        response_data["status"] = "success"
        response_data["message"] = "user created successfully"

        return response_data

    response_data = {}
    response_data["status"] = "error"
    response_data["message"] = "invalid user data"

    return response_data

    

    
