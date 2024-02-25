from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
import time


class SigninPage(PageObject):
    """
    WebElements and keywords for signinsignupPage.
    """

    _locators = {

        "cache": "//*[@class='close-btn']",
        "email_textbox": "//input[@type='email']",
        "password_textbox": "//input[@type='Password']",
        "signin_button": "//button[@class='submit']",
        "signin_page_title": "//title[text()='Admin | Sign In page.']",
        "signin_logo":"//h2[text()='Sign In']",
        "signup_page_title": "//title[text()='Signup']",
        "forgot_password":"//div/a[text()='Forgot Password?']",
        
    }

    def _is_current_page(self):
        """This function checks if the user is on the sign-in or sign-up page and returns a boolean value.
        :return: a boolean value, either True or False.
        """
        forgot_password = verify_element_on_load(self.locator.forgot_password,5)
        signin_button = verify_element_on_load(self.locator.signin_logo,5)

        if forgot_password and signin_button is True:
            print("On signin Page")
        else:
            print("signin page is not loaded correctly")
            return False
        return True

    def close_cookies_popup(self):
        """This function closes a cookies popup if it is present on the webpage.
        """
        if verify_element(self.common_locators["cache"]):
            verify_element_and_click(self.common_locators["cache"])

    def enter_user_email(self, email):
        """
        """
        if verify_element_on_load(self.locator.email_textbox) is True:
            self.se2lib.input_text(self._locators["email_textbox"], email)
        else:
            print("email address textbox is not displayed...")

    def enter_user_password(self, password):
        """This function enters a user's password into the appropriate textbox based on which page element is
        displayed.
        """
        if verify_element_on_load(self.locator.password_textbox) is True:
            self.se2lib.input_text(self._locators["password_textbox"], password)
        else:
            print("password textbox is not displayed...")

    def user_click_on_signin_button(self):
        """This function clicks on a sign-in button based on the availability of two different locators.
        """
        if verify_element_on_load(self.locator.signin_button) is True:
            self.se2lib.click_element(self._locators["signin_button"])
        else:
            print("unable to click on the signin link button")
