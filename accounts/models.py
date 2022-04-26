import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from sqlalchemy import true


# Create your models here.

#customize in models

class MyUserManager(BaseUserManager):
    def _create_user(self,contact,password,**extrafields):
        if not contact:
            raise ValueError('plz enter mobile number!!!!!')
        user = self.model(contact=contact,password=password,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,contact,password,**extrafields):
        extrafields.setdefault('is_superuser',False)
        extrafields.setdefault('role','customer')
        user=self._create_user(contact,password,**extrafields)
        return user

    def create_superuser(self,contact,password,**extrafields):
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('role','owner')
        user=self._create_user(contact,password,**extrafields)
        return user






class MyUser(AbstractBaseUser):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(null=true,unique=true)
    contact=models.BigIntegerField(unique=True)
    role=models.CharField(max_length=30)
    address=models.TextField()
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'


    # REQUIRED_FIELDS=['fname']


    
    object=MyUserManager()