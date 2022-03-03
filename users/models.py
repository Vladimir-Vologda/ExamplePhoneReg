from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


def img_dir(instance, filename):
    #   Функция записи изображений в отдельную папку для каждого пользователя
    return f'users/{instance.name}/{filename}'


class CustomUserModel(AbstractBaseUser):
    name = models.CharField(_('Username'), max_length=50, unique=True, db_index=True)
    phone = PhoneNumberField(_('Phone number'), unique=True, db_index=True)
    first_name = models.CharField(_('Name'), max_length=50, blank=True)
    last_name = models.CharField(_('Surname'), max_length=50, blank=True)
    avatar = models.ImageField(_('Image'), upload_to=img_dir, default='default/users_default.jpg')
    birthday = models.DateField(_('Birth date'), default='2001-01-01')
    registration_date = models.DateField(_('Registration date'), auto_now=True)
    is_active = models.BooleanField(_('Status active'), default=True)
    is_staff = models.BooleanField(_('Status admin'), default=False)
    slug = models.SlugField(_('URL-address'), unique=True, db_index=True)

    objects = CustomUserManager()

    #   USERNAME_FIELD - Поле используемое в качестве уникального идентификатора
    USERNAME_FIELD = 'phone'
    #   REQUIRED_FIELDS - Дополнительные обязательные поля
    REQUIRED_FIELDS = ('name',)

    class Meta:
        verbose_name = 'Пользователь(я)'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name} ({self.phone})'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        #   Функция создания slug (если slug отсутствует) для пользователя по его name
        if not self.slug:
            self.slug = slugify(self.name)
        super(CustomUserModel, self).save(**kwargs)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
