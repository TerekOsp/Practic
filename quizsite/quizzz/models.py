from django.db import models


# class Questions(models.Model):
#     id = models.IntegerField
#     question = models.CharField(max_length=200)
#
#     def __str__(self):
#         return {self.question}
#
#
# class Answers(models.Model):
#     id = models.IntegerField
#     answer = models.CharField(max_length=300)
#     isCorrect = models.CharField(max_length=20, null=True)
#
#     def __str__(self):
#         return {self.answer}


class Users(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']


    def __str__(self):
        return {self.name}

