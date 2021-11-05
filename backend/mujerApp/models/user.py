from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager (BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError ('Users must have an username')   
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    cedula = models.BigIntegerField('cedula', primary_key=True, null=False, unique=True)
    username = models.CharField('username', max_length = 20, null=False, unique=True)
    password = models.CharField('password', max_length = 256)
    nombre = models.CharField('Nombre', max_length = 50, null=False)
    direccion = models.CharField('direccion', max_length = 30, null=False)
    email = models.EmailField('Email', max_length = 100, null=False)
    telefono = models.BigIntegerField(default=0, null=False)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    