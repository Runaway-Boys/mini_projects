from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your models here.



class ScoreCards(models.Model):
    MY_CHOICES = (
    ('Postive','Postive'),
    ('Negative','Negative'),
    ('Neutral','Neutral'))
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    options = MultiSelectField(choices=MY_CHOICES,max_choices=1,max_length=200,null=True)
    def __str__(self):
        return str(self.user)
    