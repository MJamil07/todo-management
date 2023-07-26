from django.db import models

# Create your models here.

class Users(models.Model):

    # User Information
    name = models.CharField(max_length = 23 , null = False)
    email = models.EmailField(unique = True , null = False)
    password = models.CharField(max_length = 15 , null = False)
    phone = models.BigIntegerField(null = False)

    def __str__(self) -> str:
        return f'{self.name}'