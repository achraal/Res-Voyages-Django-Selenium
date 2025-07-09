from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import SeleniumTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium import webdriver
import time

class TestReservation(SeleniumTest):
    def test_login_valid(self):
        self.driver.get("http://localhost:8888/")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys("malak")
        self.driver.find_element(By.NAME, "password").send_keys("malakmalak")
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(2)
        #Formumlaire de connexion

        wait = WebDriverWait(self.driver, 10)
        voyage_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Voyages')]"))
        )

        assert voyage_element is not None
        voyage_element.click()
        time.sleep(3)
        #Catalogue des voyages


        wait = WebDriverWait(self.driver, 10)
        res_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Aventure')]//a[contains(text(), 'Réserver')]"))
        )
        res_link.click()
        time.sleep(2)
        #Page de réservation du voyage


        wait = WebDriverWait(self.driver, 10)
        res_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Réserver le circuit')]"))
        )

        assert res_element is not None
        assert "Réserver le circuit" in res_element.text
        # Verification de la présence du texte "Réserver le circuit"


        form = self.driver.find_element(By.XPATH, "(//form)[1]")


        checkbox = form.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        if not checkbox.is_selected():
            checkbox.click()

        input_number = form.find_element(By.CSS_SELECTOR, "input[type='number']")
        input_number.clear()
        input_number.send_keys("5")  # Remplacez "5" par la valeur souhaitée


        select_element = form.find_element(By.TAG_NAME, "select")
        select = Select(select_element)
        # select.select_by_value("valeur_de_l_option")
        # select.select_by_visible_text("Texte de l'option")
        select.select_by_index(1)

        time.sleep(2)  

        submit_button = form.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Reservation réussie