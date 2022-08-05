from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''тест нового посетителя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        # Эдит слышала про крутое новое онлайн-приложение со списком
        # неотложенных дел. Она решает оценить его  домашнию страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках
        # неотложенных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Она набирает в текстовом поле "Купить павлиньи перья" (её хобби -
        # вязание раболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажмиает enter, страница обновляется, и теперь страница
        # содержит "1: Купить павлиньи перья" в качестве элемента списка
        input.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлиньи перья' for row in rows)
        )

        # Текстовое поле по-прежнему приглашает её добавить ещё один элемент.
        # Она вводит "Сделать мушку из павлиньих перьев"
        # (Эдит очень методична)
        self.fail('Закончить тест!')

        # Страница снова обновляется, и теперь показывает оба элемента её списка

        # Эдит интересно, запомнит ли сайт её список. Далее она видит, что
        # сайт сгенерировал для неё уникальный URL-адрес - об этом
        # выводится небольшой текст с объяснениями.

        # Она посещает этот URL-адрес - её список по-прежнему там.

        # Удовлетворенная, она снова ложится спать
         

if __name__ == '__main__':
    unittest.main(warnings='ignore')