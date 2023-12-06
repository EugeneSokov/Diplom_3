import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument("--window-size=1500,1000")
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(options=options, service=service)

    elif request.param == 'firefox':
        service = GeckoDriverManager().install()
        browser = webdriver.Firefox(service=Service(service))

    browser.get(f"{url}")

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def create_user():
    payload = {
        "email": 'BilboBeggins1@sheer.net',
        "password": 'qwertyzxcv123',
        "name": 'Bilbo Beggins'
    }
    r_register = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", data=payload)
    token = r_register.json()["accessToken"]
    data_auth = {
         "authorization": token
    }

    yield r_register
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers=data_auth, data=payload)
