from email.policy import default

from django.db import models
from my_app.models import book
from account_app.models import UserProfile

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    items = models.ManyToManyField(book)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    book = models.ForeignKey(book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)