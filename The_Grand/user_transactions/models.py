from django.db import models
from datetime import datetime

# Create your models here.
class reviews(models.Model):
    id=models.AutoField(primary_key=True)
    comment=models.TextField()
    user= models.TextField()
    created_on=models.DateField(default=datetime.now, blank =True)

    def __str__(self) :
        return f"{self.comment}"

class rooms(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.IntegerField(default=0)
    room_type=models.TextField()
    price=models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.price}"
    # def __str__(self) :
    #     return f"{self.room_type}"

class user_booking(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.TextField()
    email=models.TextField()
    price=models.IntegerField(default=0)
    no_rooms=models.IntegerField(default=0)
    days=models.IntegerField(default=0)
    total_price=models.IntegerField(default=0)
    date1=models.DateField(default=datetime.now, blank =True)
    date2=models.DateField(default=datetime.now, blank =True)

    def __str__(self) :
        return f"{self.id}"

class restaurant(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.TextField()
    quantity=models.IntegerField(default=0)
    amount=models.IntegerField(default=0)

    def __str__(self) :
        return f"{self.amount}"

        
