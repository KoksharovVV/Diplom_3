from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(locator))

    def wait_and_click(self, locator, wait_time=10):
        element = self.find_element(locator, wait_time)
        element.click()

    def wait_for_visibility(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(locator))
        return element

    def wait_for_clickable(self, locator, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(locator))
        WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable(locator))
        return element

    def not_find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(ec.none_of(ec.visibility_of_element_located(locator)))

    def drag_and_drop_element(self, element_to_drag, target_location):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element_to_drag, target_location).perform()
