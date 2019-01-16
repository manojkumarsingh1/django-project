from django.db import models
from django.contrib.auth.models import User

# Create your models here
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User)
#this is the model class to additional info beacuse default user have only alredy some oinfo option  email,pass,first name and last name
    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
    # user uploded all profile pics will be saved into media inside profile_pic folder
