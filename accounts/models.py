from django.db import models

# Create your models here.
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    curr_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    sender_id = models.IntegerField()
    sender_name = models.CharField(max_length=100,default="")
    receiver_id = models.IntegerField()
    receiver_name = models.CharField(max_length=100,default="")
    date = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.sender_name  