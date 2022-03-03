from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, name, phone, password=None):
        """
        Создание и сохранение пользователя
        """
        #   Проверка заполнения поля name
        if not name:
            raise ValueError(_('The name must be'))

        #   Проверка заполнения поля phone
        if not phone:
            raise ValueError(_('The phone number must be'))

        user = self.model(
            name=name,
            phone=phone,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone, password=None):
        """
        Создание и сохранение суперпользователя (Администратора)
        """
        user = self.create_user(
            name=name,
            phone=phone,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
