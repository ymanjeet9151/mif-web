from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
import time


class AdminToDoList(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {
        
        "app-navigation":"//section[@class='main-content']//app-navigation",
        "Admin_to_do_list_app_navig":"//app-navigation//a[contains(text(), 'Admin To-Do')]",
        "Admin_to_do_list_app_navig_active":"//app-navigation//a[@class='active']",
        "Admin_to_do_list_heading":"//div[@class='admin-todo-list']/..//div[@class='heading mb-4']",
        
    }



    def _is_current_page(self):
        """
        This function checks if the current page is the Admin_to_do_list page by verifying the presence of specific
        elements.
        """
        Admin_to_do_list_app_navig_active = verify_element_on_load(self.locator.Admin_to_do_list_app_navig_active,5)
        Admin_to_do_list_heading = verify_element_on_load(self.locator.Admin_to_do_list_heading, 5)

        if Admin_to_do_list_app_navig_active and Admin_to_do_list_heading is True:
            print("On Admin to do list page")
        else:
            print("Admin to do list page is not loaded correctly")
            return False
        return True
  
    def user_click_on_admin_to_do_list_app_navig(self):
        """
        The function checks if the admin to-do list app navigation element is present and clicks on it if it
        is, otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            verify_element_and_click(self._locators["Admin_to_do_list_app_navig"])
        else:
            raise Exception
