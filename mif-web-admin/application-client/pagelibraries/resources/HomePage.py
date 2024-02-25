import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *


class HomePage(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {
    
        "Ad_Network_Platform_home":"//title[text()='Admin | Ad Network Platform page']",
        "Ad_Network_Platform_above_container":"//section//*[text()='MIF Ad Network Platform (Admin/Agent )']",
        "Ad_Network_Platform_container":"//div[contains(@class, 'theme-container')]",
        "advertiser_platform":"//section//*[text()='MIF ADVERTISER PLATFORM']",
        "publisher_platform":"//section//*[text()='MIF PUBLISHER PLATFORM']",
        
        
    }

    def _is_current_page(self):

        """This function checks if the current page is the home page by verifying the presence of specific
        elements.
        :return: a boolean value, either True or False.
        """
        Ad_Network_Platform_container = verify_element_on_load(self.locator.Ad_Network_Platform_container,5)
        Ad_Network_Platform_above_container = verify_element_on_load(self.locator.Ad_Network_Platform_above_container, 5)

        if Ad_Network_Platform_container and Ad_Network_Platform_above_container is True:
            print("On HomePage")
        else:
            print("Home page is not loaded correctly")
            return False
        return True

    def user_selects_platform(self,platform):
        """ This function selects the platform on main homepage based on platform arguments.
        """
        if platform =="advertiser_platform":
            self.se2lib.click_element(self._locators["advertiser_platform"])
        elif platform =="publisher_platform":
            self.se2lib.click_element(self._locators["publisher_platform"])
        else:
            print("platform not found")

