from django.test import SimpleTestCase
from django.urls import resolve,reverse
from mainapp.views import hero_section_view,project_details
from singlepage.views import strategy_view,services_view,philosophy_view,contact_view

class test_urls (SimpleTestCase):

    def test_home (self):
        url =reverse("home")
        self.assertEquals(resolve(url).func,hero_section_view)

    def test_project_details (self):
        url =reverse("project_details" ,args =[1])
        self.assertEquals(resolve(url).func,project_details)

    def test_project_details(self):
        url = reverse("project_details", args=[1])
        self.assertEquals(resolve(url).func, project_details)

    def test_philosophy(self):
        url = reverse("philo")
        self.assertEquals(resolve(url).func.view_class, philosophy_view)