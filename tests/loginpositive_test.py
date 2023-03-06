import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestPositiveLogin:

    @pytest.mark.login
    def test_charge_webpage(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")

    @pytest.mark.login
    @pytest.mark.positivelogin
    def test_positive_login(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"

    @pytest.mark.login
    @pytest.mark.negativelogin
    def test_login_incorrect_data(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin1")
        driver.find_element(By.NAME, "password").send_keys("password1")
        driver.find_element(By.NAME, "submit").click()
        wait = WebDriverWait(driver, 10)
        incorrect_message = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='red']")))
        assert incorrect_message.text == "Login Incorrect", "The message 'Login Incorrect' is not showing"
        assert driver.current_url == "http://192.168.0.108/fenix8.0/login", "The URL changed, it shouldn't change"

    @pytest.mark.login
    @pytest.mark.negativelogin
    def test_login_incorrect_user(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin1")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        incorrect_message = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='red']")))
        assert incorrect_message.text == "Login Incorrect", "The message 'Login Incorrect' is not showing"
        assert driver.current_url == "http://192.168.0.108/fenix8.0/login", "The URL changed, it shouldn't change"

    @pytest.mark.login
    @pytest.mark.negativelogin
    def test_login_incorrect_password(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password1")
        driver.find_element(By.NAME, "submit").click()
        wait = WebDriverWait(driver, 10)
        incorrect_message = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='red']")))
        assert incorrect_message.text == "Login Incorrect", "The message 'Login Incorrect' is not showing"
        assert driver.current_url == "http://192.168.0.108/fenix8.0/login", "The URL changed, it shouldn't change"

    @pytest.mark.login
    @pytest.mark.negativelogin
    def test_login_emptydata(self, driver):
        # verified if the webpage load
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/login"
