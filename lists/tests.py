from django.test import TestCase

class SmokeTest(TestCase):
    '''тест на токсичность'''

    def test_bad_maths(self):
        '''тесты: не правильные математические расчеты'''
        self.assertEqual(1 + 1, 3)