from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta


# NewsFeed Model
class NewsFeed(models.Model):
    """
    It has following columns :
        id Integer Primary Key
        url Charfield Unique
        title Charfield
        hid Charfield (HackerNewsID)
        author Charfield
        postedon Charfield Time in Strinf
        upvotes Integer
        comments Integer
    """

    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255,unique=True)
    title = models.CharField(max_length=255)
    hid = models.CharField(max_length=255,unique=True)
    author = models.CharField(max_length=50)
    posted_on = models.DateTimeField(editable=False,default=datetime.now())
    upvotes = models.IntegerField()
    comments = models.IntegerField()

    def __str__(self):
        return " "+str(self.url) + " "+str(self.title) + " "+str(self.hid)
    

class Profile(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,editable=True,blank=True)
    bday = models.DateField(editable=True,blank=True)
    email = models.EmailField(unique=True,max_length=100,blank=True)

    def get_absolute_url(self):
        return reverse("entry:profile",kwargs={"pk":self.id})
    
    def  __str__(self):
        return str(self.id) + "--" + str(self.user) + "--" + str(self.name)
    
class Bookmarks(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    hack_id = models.ForeignKey(NewsFeed,on_delete=models.DO_NOTHING)
    bid = models.AutoField(primary_key=True,auto_created=True)
    

class UserRead(models.Model):
    userid = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    hid = models.ForeignKey(NewsFeed,on_delete=models.DO_NOTHING)
    read = models.BooleanField(default=True)
    dated = models.DateTimeField(auto_now_add=True)


class UserDeleted(models.Model):
    userid = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    hid = models.ForeignKey(NewsFeed,on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add = True)


