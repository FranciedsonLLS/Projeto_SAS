from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Usuário deve ter um endereço de email.')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    cpf = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=16, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='Endereço de e-mail',
        max_length=255,
        unique=True,
    )

    # você pode adicionar mais campos, como "born_date"
    # you can add more fields, as "born_date"
    born_date = models.DateTimeField(blank=True, null=True) 
    # se você adicionar mais campos, lembre de adicioná-los aos REQUIRED_FIELDS abaixo e em fields() de "forms.py > UserCreationForm > Meta"
    # if you add more fields, remind yourself of add them to the REQUIRED_FIELDS above and on fields() from "forms.py > UserCreationForm > Meta"
    
    is_active = models.BooleanField(default=True)
    
    date_joined = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'born_date', 'cpf', 'telefone']