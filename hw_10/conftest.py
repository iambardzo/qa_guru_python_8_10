import pytest
from selene import browser

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.window_width = 1280
    browser.config.window_height = 1024
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()