from django.urls import path
from profiles_api import views

#as_view() converts tells the django to render the class based views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view(), name = 'hello-view'),
]
