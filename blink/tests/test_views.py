from django.test import TestCase,Client
from django.urls import reverse

class test_views (TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse("home")
        self.services_url = reverse("services")

    def test_hero (self):
        response = self.client.get(self.home_url)
        print(response.status_code)
        #self.assertEquals(response.status_code,200)

    def test_services (self):
        response = self.client.get(self.services_url)
        self.assertEquals(response.status_code,200)



