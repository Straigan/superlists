from urllib import response
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    '''тест домшней страници'''
    
    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает правильный html'''
#        request = HttpRequest()
#        response = home_page(request)
#        html = response.content.decode('utf8')
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')