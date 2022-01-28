
#Creating our first API

from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    ''' Test API ''' 
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

