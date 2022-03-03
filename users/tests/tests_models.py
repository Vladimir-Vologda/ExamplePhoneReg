from django.test import TestCase

from users.models import CustomUserModel

model = CustomUserModel


class TestCustomUserModel(TestCase):

    def test_fields(self):

        user = model.objects.create_user(
            phone='+75555555555', name='UserTest', password='secret_test_password'
        )

        #   verbose_name tests
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Username')
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'Номер телефона')
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Name')
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'Surname')
        field_label = user._meta.get_field('avatar').verbose_name
        self.assertEqual(field_label, 'Изображение')
        field_label = user._meta.get_field('birthday').verbose_name
        self.assertEqual(field_label, 'Birth date')
        field_label = user._meta.get_field('registration_date').verbose_name
        self.assertEqual(field_label, 'Registration date')
        field_label = user._meta.get_field('is_active').verbose_name
        self.assertEqual(field_label, 'Status active')
        field_label = user._meta.get_field('is_staff').verbose_name
        self.assertEqual(field_label, 'Status admin')
        field_label = user._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'URL-address')

        #   max_length tests
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

        #   def __str__(self): test
        expected_object_name = f'{user.name} ({user.phone})'
        self.assertEqual(expected_object_name, str(user))

        #   slug test
        expected_object_slug = user.slug
        self.assertEqual(expected_object_slug, 'usertest')

        #   unique tests
        unique = user._meta.get_field('name').unique
        self.assertTrue(unique)
        unique = user._meta.get_field('phone').unique
        self.assertTrue(unique)
        unique = user._meta.get_field('slug').unique
        self.assertTrue(unique)
