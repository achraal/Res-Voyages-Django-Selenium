from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import SeleniumTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

class TestSignup(SeleniumTest):
    def test_signup_valid(self):
        self.driver.get("http://localhost:8888/register/")
        time.sleep(2)
        
        self.driver.find_element(By.NAME, "username").send_keys("newuser")
        self.driver.find_element(By.NAME, "email").send_keys("newuser@example.com")
        self.driver.find_element(By.NAME, "password").send_keys("newpassword")
        self.driver.find_element(By.NAME, "confirm_password").send_keys("newpassword")
        self.driver.find_element(By.NAME, "preferences").send_keys("I love traveling to new places and experiencing different cultures.")
        

        time.sleep(2)  

        wait = WebDriverWait(self.driver, 10)
        submit_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), \"S'inscrire\")]"))
        )
        submit_button.click()
        time.sleep(2)

        wait = WebDriverWait(self.driver, 10)
        profil_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Profil')]"))
        )

        assert profil_element is not None
        assert "Profil" in profil_element.text
        assert "Plateforme" in self.driver.title