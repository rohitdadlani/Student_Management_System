from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


def generate_student_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique student id


class Attendence(models.Model):
    s_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    student_id = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.s_name, self.student_id)

    def save(self, *args, **kwargs):
        if len(self.student_id.strip(" "))==0:
            self.student_id = generate_student_id()

        super(Attendence, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
       return self.name
       



'''

# ---------------------------------------------------------------------------------------
from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=False,
                                        default="default-username")
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.email
# ---------------------------------------------------------------------------------------

'''