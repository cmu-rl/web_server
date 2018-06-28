from django.test import TestCase, Client, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from hb.user_server import add_user
from django.urls import reverse

class QueueTests(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_queue_home(self):
        response = self.client.get("/queue/")
        self.assertEqual(response.status_code, 200)

    def test_get_form(self):
        response = self.client.get("/queue/form")
        self.assertEqual(response.status_code, 200)
    

    def test_submission(self):
        url = '/queue/form'
        response = self.client.post(url, {'username':'Glabb', 'email': 'mirandaylchen@gmail.com','password':'123456'})
        self.assertEqual(response.status_code, 302) # sucess and redirected
        # print(response.status_code)
        # print(response.content)


    def test_fail_submission(self):
        url = '/queue/form'
        response = self.client.post(url, {'username':'yinglanc', 'email': 'mirandaylchen@gmail.com','password':'123456'})
        self.assertEqual(response.status_code, 200)


    def test_status(self):
        url = reverse('queue:status', args=("Glabb",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
