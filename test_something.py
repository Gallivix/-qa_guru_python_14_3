import pytest
from selene import browser, have


def test_valid_search(browser_setup):
    browser.open('https://ya.ru ')
    browser.element('[name=text]').type('найди мне что-то в браузере').press_enter()

def test_invalid_search(browser_setup):
    browser.open('https://ya.ru ')
    browser.element('[name=text]').type('site:example.com "1234567890abcdefghijklmnopqrstuvwxyz" mime:pdf lang:zu date:19000101').press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
    print("Ничего не найдено")