from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "test_user"
        cls.password = "Test1234!"
        cls.first_name = "James"
        cls.last_name = "Bond"

    def test_valid_license_number(self):
        form_data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "license_number": "AAA12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_license_number_too_short(self):
        form_data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "license_number": "AA12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertFalse(form.is_valid())

    def test_invalid_license_number_format_uppercase(self):
        form_data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "license_number": "abc12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertFalse(form.is_valid())

    def test_invalid_license_number_format_digits(self):
        form_data = {
            "username": self.username,
            "password1": self.password,
            "password2": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "license_number": "AAAABCDD",
        }
        form = DriverCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertFalse(form.is_valid())
