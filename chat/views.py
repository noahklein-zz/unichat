from django.shortcuts import render
from models import *


def chatroom(request, chatroom_slug):
    chatroom = Chatroom(name=chatroom_slug)
    
