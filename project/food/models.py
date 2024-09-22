from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.category_name


class User(AbstractUser):
    # username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100,default='Kozhikode')
    mobile=models.PositiveIntegerField(default='0123456789')
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100,default='')
    profile=models.ImageField(upload_to='profilepics',default='default.jpg')

class FoodMenu(models.Model):
    restaurant_name=models.CharField(max_length=100,default="RAHMATH")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    food_name=models.CharField(max_length=100)
    food_quantity=models.PositiveIntegerField()
    food_price=models.PositiveIntegerField()
    food_select_quantity=models.PositiveIntegerField(default=1)
    image=models.ImageField(upload_to='image',null=True)
    def __str__(self):
        return self.food_name
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodMenu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodMenu,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    cart=models.PositiveIntegerField()
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100,default='Kozhikode')
    mobile=models.PositiveIntegerField(default='0123456789')
class WishlistModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(FoodMenu,on_delete=models.CASCADE)
