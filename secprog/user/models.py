from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(null=False, max_length=150)
    uname = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False, max_length=150)
    contact_num = models.CharField(null=True, max_length=150)
    password = models.CharField(null=False, max_length=150)
    salt = models.CharField(null=False, max_length=255)
    picture = models.ImageField(upload_to='user/%Y/%m/%d/', default='user/default_profile.png')
    billingAdd = models.CharField(null=False, max_length=1024)
    shippingAdd = models.CharField(null=False, max_length=1024)

    def __str__(self):
        return self.uname

class PurchaseHistory(models.Model):
    def method():
        from posts.models import Item
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        item = models.ForeignKey(Item, on_delete=models.CASCADE)

class AdminUser(models.Model):
    uname = models.CharField(null=False, max_length=150)
    password = models.CharField(null=False, max_length=150)
    typeof = models.IntegerField(default=0)