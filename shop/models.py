from django.db import models

# Create your models here.

class user(models.Model):
	Name = models.CharField(max_length=100)
	Email = models.EmailField()
	phone = models.IntegerField()
	password = models.CharField(max_length=50, default="null")
	College = models.CharField(max_length=50)
	Faculty = models.CharField(max_length=30)

class book(models.Model):
	image = models.ImageField(upload_to='book/')
	Book_Name = models.CharField(max_length=100)
	Book_Description = models.CharField(max_length=500)
	Author = models.CharField(max_length=150)
	Category = models.CharField(max_length=40)
	Price = models.IntegerField()
	Seller_Name = models.CharField(max_length=100)
	Seller_Email = models.EmailField()
	Seller_Phone = models.IntegerField()
	sold = models.BooleanField(default="False")
	
class product(models.Model):
	image = models.ImageField(upload_to='product/')
	Product_Name = models.CharField(max_length=100)
	Product_Description = models.CharField(max_length=500)
	Price = models.IntegerField()
	Seller_Name = models.CharField(max_length=100)
	Seller_Email = models.EmailField()
	Seller_Phone = models.IntegerField()
	sold = models.BooleanField(default="False")