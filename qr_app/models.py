from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#........

#index.....

#feedback.....

class feed(models.Model):
     message=models.CharField(max_length=500)

#shopkeeper models start
#......
# class reguser(models.Model):
#     username=models.CharField(max_length=50)
#     password=models.CharField(max_length=30,null=True)
#     email.models.EmailField(max_length=254,null=True)
    
class shopkeeper(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    shopowner_name =models.CharField(max_length=30,null=True)
    shop_name=models.CharField(max_length=30)
    floor=models.IntegerField()
    mailadress=models.EmailField()
    password=models.CharField(max_length=30,null=True)
    confirm_password=models.CharField(max_length=30,null=True)


class Ratings(models.Model):
    shopkeepers=models.ForeignKey(shopkeeper, on_delete=models.CASCADE,null=True,blank=True)
    rating=models.IntegerField()

class Type(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

#
class Products(models.Model):
    image = models.ImageField(upload_to='images/')  # 'images/' is the directory where images will be uploaded
    product_name=models.CharField(max_length=30)
    brand_name=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    quality=models.CharField(max_length=30)
    material=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    product_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    shopkeeper = models.ForeignKey(shopkeeper, on_delete=models.CASCADE)

    # Other fields related to the Book

    def __str__(self):
        return self.product_name
#
# #food detials....
#
# class food(models.Model):
#     image=models.ImageField()
#     food_name=models.CharField(max_length=30)
#     countryfood=models.CharField(max_length=30)
#     quantityfood=models.CharField(max_length=30)
#     pricefood=models.IntegerField()
#     descriptionfood=models.CharField(max_length=100)
#
# #electronic detials...
#
# class electronic(models.Model):
#     image=models.ImageField()
#     product_name=models.CharField(max_length=30)
#     brand_name=models.CharField(max_length=30)
#     country=models.CharField(max_length=30)
#     quality=models.CharField(max_length=30)
#     color=models.CharField(max_length=30)
#     price=models.IntegerField()
#     description=models.CharField(max_length=100)
#
# #parlour detials....
#
# class parlour(models.Model):
#     image=models.ImageField()
#     product_name=models.CharField(max_length=30)
#     brand_name=models.CharField(max_length=30)
#     country=models.CharField(max_length=30)
#     quality=models.CharField(max_length=30)
#     material=models.CharField(max_length=30)
#     color=models.CharField(max_length=30)
#     price=models.IntegerField()
#     description=models.CharField(max_length=100)
#
#
#
# #funzone detials....
#
# class playzone(models.Model):
#     image=models.ImageField()
#     gamename=models.CharField(max_length=30,null=True)
#     duration=models.CharField(max_length=30,null=True)
#     price=models.IntegerField(null=True)
#     description=models.CharField(max_length=100,null=True)
#
# #theater detials..
#
# class theater(models.Model):
#     image=models.ImageField()
#     filmname=models.CharField(max_length=30)
#     show=models.CharField(max_length=30)
#     showandendtime=models.CharField(max_length=30)
#     duration=models.CharField(max_length=30)
#     price=models.IntegerField()
#     review=models.CharField(max_length=30)
#     description=models.CharField(max_length=100)
#
#
#
#
   