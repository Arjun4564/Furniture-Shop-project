from django.db import models

# Create your models here.
class Category_Db(models.Model):
    Category_name=models.CharField(max_length=200,null=True,blank=True)
    Category_image=models.ImageField(upload_to='Category_images',null=True,blank=True)
    Discription=models.TextField(max_length=200,null=True,blank=True)

class Product_Db(models.Model):
    Product_Category=models.CharField(max_length=200,null=True,blank=True)
    Product_Name=models.CharField(max_length=200,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    MRP=models.FloatField(null=True,blank=True)
    Discription=models.TextField(max_length=200,null=True,blank=True)
    Country_of_Origin=models.CharField(max_length=200,null=True,blank=True)
    Manufactured_By=models.CharField(max_length=200,null=True,blank=True)
    Product_Image1=models.ImageField(upload_to='product_images',null=True,blank=True)
    Product_Image2=models.ImageField(upload_to='product_images',null=True,blank=True)
    Product_Image3=models.ImageField(upload_to='product_images',null=True,blank=True)
    

