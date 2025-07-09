from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import SeleniumTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

class TestLogin(SeleniumTest):
    def test_login_valid(self):
        self.driver.get("http://localhost:8000/")
        time.sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys("achraf")
        self.driver.find_element(By.NAME, "password").send_keys("chouchou")
        time.sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for 2 seconds to observe the input

        wait = WebDriverWait(self.driver, 10)
        profil_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Profil')]"))
    )

        assert profil_element is not None
        assert "Profil" in profil_element.text
        assert "Plateforme" in self.driver.title

        wait = WebDriverWait(self.driver, 10)
        voyage_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Voyages')]"))
    )

        assert voyage_element is not None
        voyage_element.click()

        h2 = self.driver.find_elements(By.TAG_NAME, "h2")  # récupère toutes les divs de la page et retourne une liste

        texts = [el.text for el in h2]
        assert any("Catalogue" in text for text in texts), "Aucun <h2> ne contient 'Profil'"
        
        wait = WebDriverWait(self.driver, 10)
        logout = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Déconnexion')]"))
        )
        logout.click()