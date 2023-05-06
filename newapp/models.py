from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='book name')
    public = models.CharField(max_length=50,verbose_name='publication')
    price = models.DecimalField(max_digits=7, decimal_places=2,verbose_name='price')

    def default_price(self):
        return '$30'

    retail_price = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='sale_price',default=default_price)

    def __str__(self):
        return "title:%s pub:%s price:%s"%(self.title, self.public, self.price)

class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name='author')
    email = models.EmailField(verbose_name='email_address')

    def __str__(self):
        return 'author:%s email_address:%s'%(self.name, self.email)

class UserInfo(models.Model):
    username = models.CharField(max_length=30, verbose_name='user_name')
    password = models.CharField(max_length=30, verbose_name='pass_word')
