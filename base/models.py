from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Countrie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    _id=models.AutoField(primary_key=True,editable=False)

    fields =['_id','name']
    def __str__(self):
        return f'{self._id} , {self.name}'



class User_Role(models.Model):
    Customer='Customer'
    Airline_Company='Airline Company'
    Admin='Admin'

    ROLE_CHOICES = [
    ('Customer', 'Customer'),
    ('Airline Company', 'Airline Company'),
    ('Admin', 'Admin'),
]
    
    role_name = models.CharField(max_length=20,unique=True, choices=ROLE_CHOICES, default=Customer)

    fields =['id','role_name']
    def __str__(self):
        return f'{self._id} , {self.role_name}'



class Airline_Company(models.Model):
    _id=models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)      

    fields =['_id','name','country','user']
    def __str__(self):
        return f'{self._id} - {self.name} - {self.country}'



class Flight(models.Model):
    _id=models.BigAutoField(primary_key=True)
    airline_company =models.ForeignKey(Airline_Company, on_delete=models.CASCADE)
    origin_country =models.ForeignKey(Countrie, on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Countrie,related_name='dest_id', on_delete=models.CASCADE)
    departure=models.DateTimeField()
    landing_time=models.DateTimeField()

    fields =['_id','airline_company','origin_country','destination_country','departure','landing_time']
    def __str__(self):
        return f'{self.airline_company}'



class Customer(models.Model):
    _id=models.BigAutoField(primary_key=True)
    f_name =models.CharField(max_length=50)
    l_name =models.CharField(max_length=50)
    address =models.TextField()
    phone_No=models.CharField(max_length=12)
    credit_Card=models.CharField(max_length=16)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    fields =['_id','f_name','l_name','address','phone_No','credit_Card','user']
    def __str__(self):
        return f'{self._id} - {self.f_name} - {self.l_name} - {self.address} - {self.phone_No} - {self.credit_Card} - {self.user}'



class Ticket(models.Model):
    _id=models.BigIntegerField(primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,related_name='customer_id', on_delete=models.CASCADE)

    fields =['_id','flight','customer']
    def __str__(self):
        return  f'{self._id} - {self.flight} - {self.customer}'



class Admin(models.Model):
    _id=models.IntegerField(primary_key=True)
    f_name =models.CharField(max_length=50)
    l_name =models.CharField(max_length=50)
    user=models.ForeignKey(User ,on_delete=models.CASCADE)

    fields =['_id','f_name','l_name','user']
    def __str__(self):
        return f'{self._id} - {self.f_name} - {self.l_name} - {self.user}'




