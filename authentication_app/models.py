from django.db import models

# Create your models here.

# class createUserModel(models.Model):
#     name=models.CharField(max_length=20)
#     email=models.EmailField(unique=True)
#     number=models.IntegerField()
#     password=models.CharField(max_length=10)
    
#     userchoices=[('HR','hr'),
#                 ('EMPLOYEE','emp'),
#                 ('BDE','bde'),
#                 ('PEON','peon')]
    
#     user_type=models.CharField( max_length=20,
#                                 choices=userchoices )

#     def __str__(self):
#         return self.name
    

# class loginUserModel(models.Model):
#     email_id=models.EmailField(unique=True)
#     password=models.CharField(max_length=10)