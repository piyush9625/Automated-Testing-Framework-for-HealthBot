from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class HealthBotTestFramework(unittest.TestCase):
    """
    Automated Testing Framework for HealthBot
    """

    @classmethod
    def setUpClass(cls):
        """Setup the Selenium WebDriver and initialize resources."""
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8000")  # URL of the HealthBot application
        cls.driver.implicitly_wait(10)

    def test_home_page_loads(self):
        """Verify that the home page of HealthBot loads successfully."""
        self.assertIn("HealthBot", self.driver.title)

    def test_user_can_interact_with_bot(self):
        """Verify that a user can interact with the bot."""
        input_box = self.driver.find_element(By.ID, "chat-input")
        send_button = self.driver.find_element(By.ID, "send-button")

        input_box.send_keys("Hello, HealthBot!")
        send_button.click()

        # Validate bot's response
        response = self.driver.find_element(By.CLASS_NAME, "bot-response").text
        self.assertIn("Hello", response)

    def test_user_can_request_health_tips(self):
        """Verify that the bot provides health tips upon request."""
        input_box = self.driver.find_element(By.ID, "chat-input")
        send_button = self.driver.find_element(By.ID, "send-button")

        input_box.send_keys("Give me a health tip.")
        send_button.click()

        # Validate health tip response
        response = self.driver.find_element(By.CLASS_NAME, "bot-response").text
        self.assertTrue("tip" in response.lower())

    def test_error_handling_for_invalid_inputs(self):
        """Test bot's response to invalid or unexpected user input."""
        input_box = self.driver.find_element(By.ID, "chat-input")
        send_button = self.driver.find_element(By.ID, "send-button")

        input_box.send_keys("@@@!!!")
        send_button.click()

        # Validate error handling
        response = self.driver.find_element(By.CLASS_NAME, "bot-response").text
        self.assertIn("I didn't understand", response)

    @classmethod
    def tearDownClass(cls):
        """Clean up resources and close the browser."""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
