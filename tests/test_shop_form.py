from django.test import TestCase
from django.contrib.auth.models import User
from shop.forms import SignUpForm

class SignUpFormTests(TestCase):
    def test_register_user_with_valid_data_is_valid(self):
        form_data = { 'first_name' : 'Mohammed', 'last_name' : 'Khalil','username' : 'mkhalil' , 'email' : 'mkhalil@gfgf.com',  'password1' : '123456z!', 'password2' : '123456z!' }
        form = SignUpForm(form_data)
        self.assertTrue(form.is_valid())

    def test_register_user_with_password_mismatch_fails(self):
        form_data = { 'first_name' : 'Mohammed', 'last_name' : 'Khalil','username' : 'mkhalil' , 'email' : 'mkhalil@gfgf.com',  'password1' : '123456z!', 'password2' : '123456z'}
        form = SignUpForm(form_data)
        self.assertFalse(form.is_valid())

    def test_register_user_with_missing_data_fails(self):
        form_data = { 'first_name' : 'Mohammed','username' : 'mkhalil' , 'email' : 'mkhalil@gfgf.com',  'password1' : '123456z!', 'password2' : '123456z'}
        # Remove each key-value from dictionary, assert form not valid
        for field in form_data.keys():
            data = dict(form_data)
            del(data[field])
            form = SignUpForm(data)
            self.assertFalse(form.is_valid())

    def test_register_user_with_username_already_in_db_fails(self):

        # Create a user with username mkha
        mkha = User(username='mkha', email='mkha@kb.com')
        mkha.save()

        # attempt to create another user with same username
        form_data = { 'first_name' : 'Mohammed', 'last_name' : 'Khalil','username' : 'mkha' , 'email' : 'mkhalil@gfgf.com',  'password1' : '123456z!', 'password2' : '123456z' }
        form = SignUpForm(form_data)
        self.assertFalse(form.is_valid())