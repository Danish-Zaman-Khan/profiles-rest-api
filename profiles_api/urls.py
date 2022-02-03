from django.urls import path,include
from profiles_api import views
#importing the default router for the viewset urls
from rest_framework.routers import DefaultRouter

#Creating the router so that viewsets can be accessed
router = DefaultRouter()

#Like we register any viewset it is the std. method
router.register('hello-viewset',views.HelloViewSet,base_name = 'hello-viewset')

#registering the UserProfileViewSet to router
#Not specifying the base_name as already mentioned queryset name
#or specify if want to override the name 
router.register('profile',views.UserProfileViewSet)

#as_view() converts tells the django to render the class based views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name = 'hello-view'),
    path('login/',views.UserLoginView.as_view(), name = 'login'),
    path('',include(router.urls)) #Note:No need for the '' as we do in the urls to include the apps  #leaving the blank string because router do the work for us the router.urls creates the list for us to access all the viewsets
]
