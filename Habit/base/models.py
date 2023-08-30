from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.


# class Client(models.Model):
#     name = models.CharField(max_length=200,null = True)
#     def __str__(self):
#       return self.name

# class ScoreCard(models.Model):
#     MY_CHOICES = (
#     ('Postive','Postive'),
#     ('Negative','Negative'),
#     ('Neutral','Neutral'))
#     client = models.ForeignKey(Client,null = True,on_delete=models.CASCADE,name = "name")
#     title = models.CharField(max_length=200)
#     options = MultiSelectField(choices=MY_CHOICES,max_choices=1,max_length=200,null=True)
    
#     def __str__(self):
#         return self.title
    

class Users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
      return str(self.user)

class ScoreCards(models.Model):
    MY_CHOICES = (
    ('Postive','Postive'),
    ('Negative','Negative'),
    ('Neutral','Neutral'))
    client = models.ForeignKey(Users,null = True,on_delete=models.CASCADE,name = "name")
    title = models.CharField(max_length=200)
    options = MultiSelectField(choices=MY_CHOICES,max_choices=1,max_length=200,null=True)
    
    def __str__(self):
        return self.title

