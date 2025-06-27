from django.db import models

# Create your models here.


category = (('printtshirtm','Printtshirtm'),("shirtm","Shirtm"),("jeansm","Jeansm"),("cargom","Cargom"),
           ('baggym','Baggam'),("fullm","Fullm"),("printtshirtw",'Printtshirtw'),("hoodies","Hoodies"),("shirtw","Shirtw"),("kurta","Kurtaw"),("cargow","Cargow"),('sareesw',"Sareesw"),("braclets","Braclets"),("necklace","Necklace"),("caps","Caps"),("rings","Rings"),("sunglasses","Sunglasses"),("bags","Bags"),("watchm","Watchm"),("watchw","Watchw"),('shoes','Shoes'),('shoesw','Shoesw'))


class clothes(models.Model):
    clothname = models.CharField(max_length=100)
    clothprice = models.IntegerField()
    clothescat = models.CharField(choices=category,max_length=200)
    clothesdesc = models.TextField()
    clothimg = models.ImageField()
    clothsize = models.CharField(max_length=100,default=[],null=True)

class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100,null=True)
    address = models.TextField()
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    
    cart = models.CharField(max_length=255,default='[]')
    likes = models.CharField(max_length=255,default='[]')