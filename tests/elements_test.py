import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestElements:

    @pytest.mark.store
    def test_choose_open_store(self, driver):
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//ul[@id='storeline']/a[1]").click()
        assert driver.find_element(By.TAG_NAME, "h1").text == "PARALLEVAR"

    @pytest.mark.store
    def test_choose_close_store(self, driver):
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//ul[@id='storeline']/a[2]").click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "CashinHand")))

