
from django.db import models

# Create your models here.


class ChatDB(models.Model):
    content = models.CharField(max_length=200,default="None")
    Dtime = models.DateTimeField(auto_now=True)
    Group = models.ForeignKey("GroupDB", on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class GroupDB(models.Model):
    Dtime = models.DateTimeField(auto_now=True)
    Name = models.CharField(max_length=200) 

    def __str__(self):
        return self.Name
