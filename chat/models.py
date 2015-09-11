from django.db import models


class Chatroom(models.Model):
    name = models.CharField(max_length=32)
    occupants = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Message(models.Model):
    chatroom = models.ForeignKey(Chatroom)
    username = models.CharField(max_length=32)
    text = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
