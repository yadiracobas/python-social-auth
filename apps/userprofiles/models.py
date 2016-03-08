# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError

class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        
        try:
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            """Si ya existe el usuario no lo vuelve a guardar,
            esto es para las redes sociales, por si se trata de
            iniciar session con diferentes redes sociales que
            creadas con el mismo correo electrónico."""
            user = User.objects.get(email = extra_fields['email'])
            return user

    def create_user(self, username, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    
    #personal information
    email = models.EmailField(
						    	verbose_name='Correo electrónico',
						        max_length=255,
                                unique = True,
						        help_text = 'Debe introducir un nombre de usuario válido',
						    )
    username = models.CharField(verbose_name = 'Nombre de usuario', 
    							max_length = 50, 
    							unique = True,
                                null = True,
                                blank = True,
    							help_text = 'Se debe introducir 30 caracteres o menos')

    first_name = models.CharField(verbose_name = 'Nombre', max_length = 100)
    last_name = models.CharField(verbose_name = 'Apellido Paterno', max_length = 100)
    last_mom_name = models.CharField(verbose_name = 'Apellido Materno', max_length = 100, blank = True, null = True)
    gender_opts = ( ('M', 'Masculino'), ('F', 'Femenino'), )
    gender = models.CharField(verbose_name = 'Género', max_length = 1, choices=gender_opts, default='M')
    mobile_no = models.CharField(verbose_name = 'Teléfono', max_length = 25, blank = True, null = True)
    date_of_birth = models.DateField(verbose_name = 'Fecha de nacimiento', null = True, blank = True)
    avatar = models.ImageField('Avatar', upload_to='static/img/avatars', null = True, blank = True)

    # Additional Information
    created = models.DateTimeField(verbose_name = 'Creado', editable = False, auto_now_add = True)
    modified = models.DateTimeField(verbose_name = 'Actualizado', editable = False, auto_now = True)

    #administrative information
    is_active = models.BooleanField(verbose_name = 'Activo', default=True)
    is_admin = models.BooleanField(verbose_name = 'Administrador', default=False)
    is_superuser = models.BooleanField(verbose_name = 'Super Usuario', default=False)
    groups = models.ManyToManyField(Group,verbose_name ='Grupos',blank=True)
    user_permissions = models.ManyToManyField(Permission,verbose_name= 'Permisos', blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.last_mom_name

    def get_short_name(self):
        return self.first_name + ' ' + self.last_name

    def get_full_last_name(self):
        return str(self.last_name) + str(self.last_mom_name)

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ["last_name", "first_name"]
