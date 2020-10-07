from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin


class UserManager(BaseUserManager):


    def create_user(self, email, password=None, **extra_fields):
        """ Create and save new users """

        # lets validate the email so our test for None email wont fail
        if not email:
            raise ValueError("User must have an email.")

        # calling normalize_email here will save the email in lower case
        # which is gonna be good for when making test and to allow the users
        # login with lowercase email only.
        email=self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """ Create and save new superusers """

        user = self.create_user(email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user that support using email instead of username """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
