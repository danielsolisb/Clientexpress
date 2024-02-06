from django.db import models
from Clientexpress.settings import MEDIA_ROOT, BASE_DIR, STATIC_URL, MEDIA_URL

from django.db.models.fields import EmailField
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
from django.db.models.query import FlatValuesListIterable
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(AbstractUser):
    id_ced          = models.CharField(max_length=20, verbose_name="ID Number", unique=True, null=True, blank=True)
    address         = models.CharField(max_length=150, verbose_name="Address", null=True, blank="True") 
    telephone       = models.CharField(max_length=50, verbose_name="Telephone",blank=True, null=True)
    country         = models.CharField(max_length=30, verbose_name="Country", null=False, blank=False)
    email           = models.EmailField(unique=True, max_length=70, null=False, blank=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'password']
    def __str__(self):
        return self.get_full_name()
    
    def get_user_login(self):
        return str(self.pk)
    
    