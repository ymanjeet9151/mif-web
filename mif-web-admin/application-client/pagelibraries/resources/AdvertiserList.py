from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
import time


class AdvertiserList(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {

        "list_advertiser_heading":"//div[@class='heading']//span[text()='List Advertisers']",
        "drop_down_Menu_Button":"//div[@class='adv-dropdown']/a",
        "advertiser_dropdown_popup_enabled":"//a[@class='dropdown-toggle show']//..//ul[@class='dropdown-menu show']",
        "dropdown_profile":"//a[@class='dropdown-toggle show']//..//a[text()='Profile']",
        "dropdown_contract_financial":"//a[@class='dropdown-toggle show']//..//a[text()='Contracts/Financial Terms']",
        "dropdown_product_offer_Ads":"//a[@class='dropdown-toggle show']//..//a[text()='Product Offer Ads/Assets']",
        "dropdown_campaigns":"//a[@class='dropdown-toggle show']//..//a[text()='Campaigns']",
        "app-navigation":"//section[@class='main-content']//app-navigation",       
        "Advertiser_List_app_navig":"//app-navigation//a[text()='Advertiser List']",
        "Advertiser_List_app_navig_active":"//app-navigation//a[@class='active']/..//a[text()='Advertiser List']",
        
    
    }



    def _is_current_page(self):
        """
        This function checks if the current page is the Admin Advertiser List Page by verifying the presence of specific
        elements.
        """
        Advertiser_List_app_navig_active = verify_element_on_load(self.locator.Advertiser_List_app_navig_active,5)
        list_advertiser_heading = verify_element_on_load(self.locator.list_advertiser_heading, 5)

        if Advertiser_List_app_navig_active and list_advertiser_heading is True:
            print("On Admin Advertiser List Page")
        else:
            print("Admin Advertiser List Page is not loaded correctly")
            return False
        return True

    def user_selects_profile_menu_under_advtr_name(self):
        """ This function selects an option from a dropdown menu and performs a corresponding action.
        """
        verify_element_and_click(self._locators["drop_down_Menu_Button"],3)
        if verify_element_on_load(self._locators["advertiser_dropdown_popup_enabled"]):
            self.se2lib.click_element(self._locators["dropdown_profile"])
        else:
            print("dropdown_profile is not displayed...")
        time.sleep(4)

    def user_selects_contract_financial_menu_under_advtr_name(self):
        """ This function selects an option from a dropdown menu and performs a corresponding action.
        """
        verify_element_and_click(self._locators["drop_down_Menu_Button"],3)
        if verify_element_on_load(self._locators["advertiser_dropdown_popup_enabled"]):
            self.se2lib.click_element(self._locators["dropdown_contract_financial"])
        else:
            print("dropdown_contract_financial is not displayed...")
        time.sleep(4)
    
    def user_selects_product_offer_Ads_menu_under_advtr_name(self):
        """ This function selects an option from a dropdown menu and performs a corresponding action.
        """
        verify_element_and_click(self._locators["drop_down_Menu_Button"],3)
        if verify_element_on_load(self._locators["advertiser_dropdown_popup_enabled"]):
            self.se2lib.click_element(self._locators["dropdown_product_offer_Ads"])
        else:
            print("dropdown_product_offer_Ads is not displayed...")
        time.sleep(4)

    def user_selects_campaigns_under_advtr_name(self):
        """ This function selects an option from a dropdown menu and performs a corresponding action.
        """
        verify_element_and_click(self._locators["drop_down_Menu_Button"],3)
        if verify_element_on_load(self._locators["advertiser_dropdown_popup_enabled"]):
            self.se2lib.click_element(self._locators["dropdown_campaigns"])
        else:
            print("dropdown_campaigns is not displayed...")
        time.sleep(4)

    def user_click_on_advertiser_list_app_navig(self):
        """The function checks if an element is loaded and then clicks on the "Advertiser List" app navigation.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            verify_element_and_click(self._locators["Advertiser_List_app_navig"])
        else:
            raise Exception
