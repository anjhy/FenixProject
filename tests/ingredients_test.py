import time
import pytest
from selenium.webdriver.common.by import By


class TestElements:


    @pytest.mark.ingredient
    def test_add_ingredient(self, driver):
        driver.maximize_window()
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//a[@href='http://192.168.0.108/fenix8.0/ingredients']").click();
        driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
        driver.find_element(By.ID, "IngredientCode").send_keys("0070")
        driver.find_element(By.ID, "IngredientName").send_keys("Tomato")
        driver.find_element(By.ID, "Cost").send_keys("3")
        driver.find_element(By.ID, "Unit").send_keys("10")
        driver.find_element(By.ID, "AlertQt").send_keys("3")
        driver.find_element(By.ID, "Quantity").send_keys("30")
        driver.find_element(By.CSS_SELECTOR, ".modal-footer:nth-child(2) > .btn-add").click()
        driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
        time.sleep(2)

    @pytest.mark.ingredient
    def test_close_ingredient(self, driver):
        driver.maximize_window()
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//a[@href='http://192.168.0.108/fenix8.0/ingredients']").click();
        driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
        driver.find_element(By.ID, "IngredientCode").send_keys("0070")
        driver.find_element(By.ID, "IngredientName").send_keys("Tomato")
        driver.find_element(By.ID, "Cost").send_keys("3")
        driver.find_element(By.ID, "Unit").send_keys("10")
        driver.find_element(By.ID, "AlertQt").send_keys("3")
        driver.find_element(By.ID, "Quantity").send_keys("30")
        driver.find_element(By.CSS_SELECTOR, ".modal-footer:nth-child(2) > .btn-default").click()


    @pytest.mark.ingredient
    def test_edit_ingredient(self, driver):
        driver.maximize_window()
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//a[@href='http://192.168.0.108/fenix8.0/ingredients']").click();
        driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
        driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .btn:nth-child(2)").click()
        driver.find_element(By.ID, "IngredientName").send_keys("Tomatoes")
        driver.find_element(By.ID, "PurchasePrice").send_keys("3")
        driver.find_element(By.ID, "Cost").send_keys("3")
        driver.find_element(By.ID, "Unit").send_keys("100")
        driver.find_element(By.ID, "Quantity").send_keys("302")
        driver.find_element(By.ID, "AlertQt").send_keys("15")
        driver.find_element(By.CSS_SELECTOR, ".btn-add").click()
        driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()


    @pytest.mark.ingredient
    def test_delete_ingredient(self, driver):
        driver.maximize_window()
        driver.get("http://192.168.0.108/fenix8.0/login")
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("password")
        driver.find_element(By.NAME, "submit").click()
        assert driver.current_url == "http://192.168.0.108/fenix8.0/"
        driver.find_element(By.XPATH, "//a[@href='http://192.168.0.108/fenix8.0/ingredients']").click();
        driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
        driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) .fa-times").click()
        driver.find_element(By.LINK_TEXT, "Yes, delete it!").click()
        driver.find_element(By.CSS_SELECTOR, ".sorting_asc").click()
        time.sleep(2)


