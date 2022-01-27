from django.contrib import admin

#importing the models from the app
from profiles_api import models

admin.site.register(models.UserProfile)
# Register your models here.
