# Generated by Django 4.0.3 on 2022-03-03 09:57

from django.db import migrations, models
import phonenumber_field.modelfields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, unique=True, verbose_name='Phone number')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Surname')),
                ('avatar', models.ImageField(default='default/users_default.jpg', upload_to=users.models.img_dir, verbose_name='Image')),
                ('birthday', models.DateField(default='2001-01-01', verbose_name='Birth date')),
                ('registration_date', models.DateField(auto_now=True, verbose_name='Registration date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Status admin')),
                ('slug', models.SlugField(unique=True, verbose_name='URL-address')),
            ],
            options={
                'verbose_name': 'Пользователь(я)',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]