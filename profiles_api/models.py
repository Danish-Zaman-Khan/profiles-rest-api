from django.db import models

#importing the classes that needs to be imported while overriding the User models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#importing the default manager provided by django to override
from django.contrib.auth.models import BaseUserManager

#Creating the custom User manager that takes email to create and control users
class UserProfileManager(BaseUserManager):

    '''Manager for user profiles'''

    def create_user(self, email, name, password = None):
        '''Create a new user profile'''

        #Raising exception error if email field is empty string
        if not email:
            raise ValueError('User must have an email email adderess')
        #Normalizing the email adderess i.e second part of email will be all in lower case
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        #saving the user
        user.save(using = self._db)
        #Returning the user
        return user

    def create_super_user(self, email , name, password): #we want each super user must have password
        '''Create and save new super user with given details'''
        user = self.create_user(email, name, password) #As we are calling the method inside the another method of same class so self is automatically passed -- django documentation
        user.is_superuser = True
        user.is_staff = True
        #saving the user
        user.save(using=self._db)
        #Returning the user
        return user



# Creating the User class
class UserProfile(AbstractBaseUser, PermissionsMixin):

    """
    Database model for users in the system
    """

    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True) #To check if the user profile is active or not and the default is True but can change is to false
    is_staff = models.BooleanField(default=False) # This determines if the user is staff user so that the user can have required access by default it is False but we can check True for the users who are the staff.

    objects = UserProfileManager()  #Custom model manager to create and control users

    USERNAME_FIELD = 'email' #It will be compulsory the field we are overriding the username
    REQUIRED_FIELDS = ['name'] #Additional fields that are REQUIRED_FIELDS

    #To get the full name of the users
    def get_full_name(self):
        '''Retrive the full name of the user '''

        return self.NAME

    def get_short_name(self):

        '''Retrive the short name of the user'''

        return self.name #As we don't have the shortname field so we are returning the name

    def __str__(self):

        '''Retrive the string representation of user'''

        return self.email  #This will show the model with email in the list
