from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __str__(self):
        return '%s' %(self.user)
class product(models.Model):
    product_name  = models.CharField("name",max_length=25)
    product_price = models.IntegerField()
    user          = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
    def __str__(self):
        return '%s' %(self.product_name)
