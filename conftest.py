import pytest
from selene import browser

@pytest.fixture(scope = "session")
def browser_setup():
    # Устанавливаем размер окна браузера
    browser.config.window_width = 1440
    browser.config.window_height = 900
    print("Применяем фикстуру с размером экрана")
    yield

    print("Закрываем браузер")