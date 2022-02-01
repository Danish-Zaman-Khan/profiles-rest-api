#creating the permission for the user for proper authentication 

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to update there own profiles'''
    #Below function will return boolean value according the conditions meet
    
    def has_object_permission(self, request, view, obj):
        '''Check whether the user is updating his own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True
        #Return True or false according the below condition 
        return obj.id == request.user.id
    
    