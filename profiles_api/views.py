
#Creating our first API

from rest_framework.views import APIView
from rest_framework.views import Response
#To get the status of response if the response is bad
from rest_framework import status   
#importing the serializer we created 
from profiles_api import serializer

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
