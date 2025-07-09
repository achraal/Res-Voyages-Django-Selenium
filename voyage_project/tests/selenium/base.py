from selenium import webdriver

class SeleniumTest:
    def setup_method(self):
        self.driver = webdriver.Firefox()  # geckodriver sera trouvé automatiquement via le PATH
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
