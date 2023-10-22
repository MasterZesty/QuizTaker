from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    # base class fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # set tbase model as abstract so this model will
    # not be used to crete any dtabase table. Instead, 
    # when it is used as a base class for other models, 
    # its fields will be added to those of the child class.
    class Meta:
        abstract = True

class User(BaseModel):
    email = models.EmailField(unique=True, max_length=255, null=False)
    name  = models.CharField(max_length=65, null=False)
    password = models.CharField(max_length=100, null=False)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False, db_column='user_id')

    class Meta:
        verbose_name_plural = "Users"
        db_table = "quiz_builder_users"

    def __str__(self):
        return f'{self.name}'

class Quiz(BaseModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    quiz_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='quiz_id')
    quiz_title = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Quizs"
        db_table = "quiz_builder_quiz"

    
    def __str__(self):
        return f'{self.quiz_title}'

class QuizQuestion(BaseModel):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, db_column='quiz_id')
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=255, null=False)
    option_a = models.CharField(max_length=255, null=False)
    option_b = models.CharField(max_length=255, null=False)
    option_c = models.CharField(max_length=255, null=False)
    option_d = models.CharField(max_length=255, null=False)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=False)

    class Meta:
        verbose_name_plural = "Quiz Questions"
        db_table = "quiz_builder_quiz_question"

    def __str__(self):
        return f'{self.question}'

