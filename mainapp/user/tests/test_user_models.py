from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email='test@gmail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email=email, password=password)


class UserModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test for creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = 'testpass'
        user = sample_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = sample_user(email, "test12345")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            sample_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='test123456',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
