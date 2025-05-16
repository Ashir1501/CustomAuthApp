from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email=None, password = None):
        if not email:
            raise ValueError('Users must have username')
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email)
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, first_name, last_name, email=None, password=None):
        user = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser =  True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to="images", blank=True, null=True)
    username = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=150, unique=True, null=False)
    # address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name","last_name","email"]

    def __str__(self):
        return self.username
    

class Address(models.Model):
    line_1 = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=100, blank=False, null=True)
    state = models.CharField(max_length=50, blank=False, null=True)
    pin_code = models.CharField(max_length=20, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)