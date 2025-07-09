from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import SeleniumTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium import webdriver
import time

class TestFacture(SeleniumTest):
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
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Mes Voyages')]"))
        )
        voyage_element.click()

        time.sleep(3)

        wait = WebDriverWait(self.driver, 10)
        ligne = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tr[td[contains(text(), 'Aventure')]]"))
        )

        lien = ligne.find_element(By.XPATH, ".//a[contains(text(), 'Facture')]")
        lien.click()


        wait = WebDriverWait(self.driver, 10)
        paiement_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Facture')]"))
        )

        assert paiement_element is not None
        assert "Facture" in paiement_element.text