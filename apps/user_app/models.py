from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
class user_manager(models.Manager):
    def user_validation(self, PostData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        error = []
        if (len(PostData['name']) <1):
            error.append('name must be longer the zero charectors')
        if (len(PostData['username']) < 5):
            error.append('UserName MUST be LONGER then 5 charectors')
        if (len(PostData['password'])<8):
            error.append('password too short dip shit(dont get hacked)')
        if PostData['password']!= PostData['re-password']:
            error.append('password do not match')

        try:
            if not EMAIL_REGEX.match(PostData['email']):
                error.append('invalid email')
        except ValueError:
            error.append('no email enterd')
        if len(error)>0:
            return (False,error)
        else:
            hashed = bcrypt.hashpw(PostData['password'].encode('utf8'), bcrypt.gensalt())
            user = userReg.objects.create(name=PostData['name'], username = PostData['username'],email = PostData['email'],password=hashed)
            return (True, user)

    def login_validation(self, PostData):
        error=[]
        if (len(PostData['username']) < 5):
            error.append('not a valid username')
        if (len(PostData['password']) < 8):
            error.append('wrong password')
        if len(error) > 0:
            return (False, error)
        else:
            checkPassword = userReg.objects.filter(username=PostData['username'])
            if checkPassword:
                if bcrypt.checkpw(PostData['password'].encode(), checkPassword[0].password.encode()):
                    return (True, checkPassword)
                else:
                    error.append('password invalid')
            else:
                error.append('wrong username dipshit')
            return(False,error)

        
class userReg(models.Model):
    name= models.CharField(max_length=234)  
    username= models.CharField(max_length=234)
    password= models.SlugField(max_length=200)
    email = models.CharField(max_length=60)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    objects = user_manager()