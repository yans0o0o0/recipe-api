from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Creating a new user with email is successfully """
        email="yans@gmail.com"
        password="user123"

        user = get_user_model().objects.create_user(
           email=email,
           password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
           email='test@gmail.com',
           password='test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    def test_new_user_email_normalize(self):
        """ Test if email for new user is normalized """
        email = 'testemail@UPPERCASE.COM'
        user = get_user_model().objects.create_user(email,'pass123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"pass123")
