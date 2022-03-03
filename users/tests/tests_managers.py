from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class TestManager(TestCase):

    def test_create_user(self):
        self.phone = '+79999999999'
        self.name = 'TestUser'
        self.password = 'secret_password'

        user = User.objects.create_user(
            phone=self.phone, name=self.name, password=self.password
        )

        self.assertEqual(user.phone, '+79999999999')
        self.assertEqual(user.name, 'TestUser')
        self.assertEqual(user.slug, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertNotEqual(user.phone, '+78888888888')
        self.assertNotEqual(user.name, 'NoTestUser')

        with self.assertRaises(TypeError):
            User.objects.create_user(

            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone='', name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone=self.phone, name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_user(
                phone='', name=self.name, password=''
            )

    def test_create_superuser(self):
        self.phone = '+77777777777'
        self.name = 'TestSuperUser'
        self.password = 'secret_super_password'

        super_user = User.objects.create_superuser(
            phone=self.phone, name=self.name, password=self.password
        )

        self.assertEqual(super_user.phone, '+77777777777')
        self.assertEqual(super_user.name, 'TestSuperUser')
        self.assertEqual(super_user.slug, 'testsuperuser')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertNotEqual(super_user.phone, '+76666666666')
        self.assertNotEqual(super_user.name, 'NoTestSuperUser')

        with self.assertRaises(TypeError):
            User.objects.create_superuser(

            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone='', name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone=self.phone, name='', password=''
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                phone='', name=self.name, password=''
            )
