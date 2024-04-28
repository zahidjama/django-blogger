from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
from ckeditor.fields import RichTextField
# Create your models here.

class CustomUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="Email Addresss", max_length=100, unique=True)
    name=models.CharField(max_length=100, verbose_name="Full Name")
    phone=models.IntegerField(verbose_name="Phone Number ")
    joined_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    object=CustomUserManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['name', "phone",]

    def has_perm(self, perm, obj=None):
         return self.is_superuser

    def has_module_perms(self, app_label):
         return self.is_superuser

    def __str__(self):
        return self.name


class blogs(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(verbose_name="Title", max_length=150)
    image=models.ImageField(upload_to="media/")
    content=RichTextField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    uploader=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
