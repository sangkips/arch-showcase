from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UsermanagerTest(TestCase):
    def create_test_user(self):
        User = get_user_model
        user = User.objects.create_user(email='test@example.com', password='pass123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='pass123')

    def create_test_superuser(self):
        User = get_user_model
        user_admin = User.objects.create_superuser(email='admin@example.com', password='pass123')
        self.assertEqual(user_admin.email, 'admin@example.com')
        self.assertTrue(user_admin.is_active)
        self.assertTrue(user_admin.is_superuser)
        self.assertTrue(user_admin.is_staff)

        try:
            self.assertIsNone(user_admin.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='admin@example.com',
                password = 'pass123',
                is_superuser = False
            )
    
