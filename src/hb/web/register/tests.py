from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from hb.user_server import add_user
from django.urls import reverse

class SignupTests(TestCase):
    def test_signup_home(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    def test_get_form(self):
        response = self.client.get("/signup/form")
        self.assertEqual(response.status_code, 200)
    

    def test_fail_submission(self):
        url = '/signup/form'
        # password does not match
        response = self.client.post(url, {'username':'cth451', 'email': 'mirandaylchen@gmail.com','password':'123456','repwd':'654321'})
        self.assertEqual(response.status_code, 200)

    def test_faile_submission2(self):
        url = '/signup/form'
        # wrong email
        response = self.client.post(url, {'username':'cth451', 'email': 'mirandaylchen@com','password':'123456','repwd':'123456'})
        self.assertEqual(response.status_code, 200)

    def test_submission(self):
        url = '/signup/form'
        # password does not match
        response = self.client.post(url, {'username':'cth451', 'email': 'mirandaylchen@gmail.com','password':'123456','repwd':'123456'})
        print(response.content)
        self.assertEqual(response.status_code, 302)


# class AccountTestCase(LiveServerTestCase):

#     def setUp(self):
#         self.selenium = webdriver.Firefox()
#         super(AccountTestCase, self).setUp()

#     def tearDown(self):
#         selenium.selenium.quit()
#         super(AccountTestCase, self).tearDown()

#     def test_register(self):
#         selenium = self.selenium
#         # open the link we want to test
#         selenium.get('htt[://127.0.0.1:8000/signup/form')
#         # find the form element
#         username = selenium.find_element_by_id('id_username')
#         email = selenium.find_element_by_id('id_email')
#         password = selenium.find_element_by_id('id_password')
#         repwd = selenium.find_element_by_id('id_repwd')

#         submit = selenium.find_element_by_id('submit')

#         # Fill the form with data
#         username.send_keys('Glabb')
#         email.send_keys('mirandaylchen@gmail.com')
#         password.send_keys('123456')
#         repwd.send_keys('123456')

#         #submitting the form
#         submit.send_keys(Keys.RETURN)

#         # check the returned result
#         print(selenium.page_source)