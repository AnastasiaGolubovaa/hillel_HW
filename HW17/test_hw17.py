import pytest
from selenium import webdriver
from selenium.webdriver.common.options import Options
from selenium.webdriver.common.by import By



@pytest.fixture()
def get_driver(chrome):
    driver: chrome
    driver.get("https://demoqa.com/text-box")

    
