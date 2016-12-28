from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Trade(models.Model):
    item = Item

class TradeItems(models.Model):
    itemFirst = models.ForeignKey(Item, related_name='item1')
    userFirst = models.ForeignKey(User, related_name='user1')
    itemSecond = models.ForeignKey(Item, related_name='item2')
    userSecond = models.ForeignKey(User, related_name='user2')

class BlackBox(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
