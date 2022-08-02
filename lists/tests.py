from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    '''тест домшней страници'''

    def test_root_url_resolves_to_home_page_view(self):
        '''корневой url преобразовывается в представление
           домшней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)