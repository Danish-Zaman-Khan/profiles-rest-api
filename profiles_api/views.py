
#Creating our first API
from rest_framework.views import APIView

from rest_framework.views import Response

#To get the status of response if the response is bad
from rest_framework import status

#for creating the basic viewset we will import viewset
from rest_framework import viewsets

#improting classes to obtain authentication token
from rest_framework.authtoken.views import ObtainAuthToken
#Also importing the settings for add render class in our auth token in order to import default render class
from rest_framework.settings import api_settings

#importing the serializer we created
from profiles_api import serializer

#importing the models
from profiles_api import models

#Importing for the authentication
from rest_framework.authentication import TokenAuthentication

#Importing the additional permission to handle the feed
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

#Resting the api so only the authenticated users only  can view it
from rest_framework.permissions import IsAuthenticated

#importing the filter class in order to provide the search ability
from rest_framework import filters

#importing the permission we created manually
from profiles_api import permissions

class HelloApiView(APIView):
    ''' Test API '''

    #Configures our API view with the serializer we created
    serializer_class = serializer.HelloSerializer

    def get(self, request, format = None):
        '''Returns list of API views features'''
        an_apiview = [
            'uses http methods as functions(get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS'
            ]
        # Returning the response
        # Response should contain the list or dictionary
        return Response(
            {
            'message' : 'Hello!!',
            'an_apiview' : an_apiview
            }
                        )

    def post(self, request):

        '''Create hello massage with out name '''

        serializer = self.serializer_class(data = request.data)

        #Django framework provides the functionality to validate
        if serializer.is_valid():
            #We can retrieve any field we define in serializer this way like name field
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'  #f string functionality to insert name in the string
            return Response({'message': message})
        else:
            #respones by default return http_200_okay
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        #pk is for the id we are updating
        '''Handle updating an object'''
        return Response({'message':'PUT'})

    def patch(self, request, pk = None):
        '''Handle partial update of an object'''
        return Response({'message':'PATCH'})

    def delete(self, request, pk= None):
        '''Delete an object'''
        return Response({'message':'Delete'})


#Creating the Viewset
class HelloViewSet(viewsets.ViewSet):
    '''Test API Viewset'''
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        '''Returns Hello Message'''

        a_viewset = [
            'Uses the actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using routers',
            'provides more functionality with less code'
        ]

        return Response({'message':'Hello!!','a_viewset':a_viewset})

    #adding the other functions
    def create(self, request):
        '''Create a new hello Message'''
        #importing the serializer like we did above we will use same serializer here for test purpose

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            #We can get any field like below
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        '''Handle getting an object by its ID'''
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        '''Handle updating an object'''
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        '''Handle partial update of an object'''
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk= None):
        '''delete an object'''
        return Response({'http_method':'Delete'})

#using the model viewset to handle the model
class UserProfileViewSet(viewsets.ModelViewSet):

    '''Handle creating and updating profiles'''
    #Configuring the serializer for the viewset
    serializer_class = serializer.UserProfileSerializer
    #Specifying the which objects we gonna manage with the viewset
    queryset = models.UserProfile.objects.all()
    #Creating the proper authentication
    #We can add multiple authentication classes below using , to create tuple
    authentication_classes = (TokenAuthentication,)
    #We can add multiple permission classes below using , to create tuple
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    #Specifying the field with which we can search
    search_fields = ('name','email',)


#Creating the endpoints for our viewset

class UserLoginView(ObtainAuthToken):

    '''Handle creating the user authentication'''
    #We need this in order enable the ObtainAuthToken class
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# Creating the viewset for the UserProfileFeed

class UserProfileFeedViewSet(viewsets.ModelViewSet):

    ''' Handling the creating, reading and updating profile feed items'''

    #adding the authentication method
    authentication_classes = (TokenAuthentication,)
    #adding the serializer
    serializer_class = serializer.ProfileFeedItemSerializer
    #adding the model to which the viewset will be connected
    queryset = models.UserProfileFeedItem.objects.all() #This will manage the UserProfileFeedItem object
    #Adding the permissions for the viewsets
    permission_classes = {
        permissions.UpdateOwnStatus, #Permission we created
        IsAuthenticated
    }

    def perform_create(self, serializer):

        '''sets the user profile to logged in user '''

        serializer.save(user_profile = self.request.user)
