
from rest_framework import serializers
#importing the models
from profiles_api import models

class HelloSerializer(serializers.Serializer):

    '''Serializer a name field for testing our API view'''

    name = serializers.CharField(max_length= 10)

#Creating the user profile serializer

class UserProfileSerializer(serializers.ModelSerializer):

    '''Serializes the User Profile object'''

    #Using Meta class for customizing the serializer to particular model

    class Meta:
        model = models.UserProfile
        #Specifying the fields
        fields = ('id','name','email','password')
        #Using exception for the password so that the password can be entered only during user creation time

        extra_kwargs = {
            'password':{
                'write_only' : True,
                'style' : {'input_type':'password'}
            }
        }
    #Overridding the create function so that password can be saved in hashed form

    def create(self, validated_data):
        '''Create and return new user'''
        #objects is variable usedin UserProfile class indicating UserProfileManager from where we took create_user() method
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    #Below will override the default update() method so that the password after update stored in hashed form

    def update(self, instance, validated_data):

        '''Handle updating user account '''

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)

# Creating the serializer for the UserProfileFeedItem
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    '''Serializer for the profile feed item'''

    # Creating the meta class for the serializer to connect the model
    class Meta:
        model = models.UserProfileFeedItem
        #id is generated automatically to use as a Primary key in DB
        #Hence it is read only
        fields = ('id','user_profile','status_text','created_on')
        #Customizing the required fields below is the standered method
        #As for the security purpose we don't want user to create the feed and assign it to another user it will be security problem
        extra_kwargs = {
        'user_profile' : {'read_only' : True}
        }
