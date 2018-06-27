from django.test import TestCase, Client
from hb.user_server import add_user
from django.urls import reverse

class SignupTests(TestCase):
    def test_signup_home(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)

    def test_get_form(self):
        response = self.client.get("/signup/form")
        self.assertEqual(response.status_code, 200)
    

    def test_submission(self):
        url = '/signup/form'
        response = self.client.post(url, {'username':'randa'})
        self.assertEqual(response.status_code, 200)
        print(response.content)