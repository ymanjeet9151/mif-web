import time
from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *


class AdminAdvertiserHome(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {
    
        "advertiser_home_page_title":"//title[text()='Advertisers Home']",
        "advertiser_home_heading":"//div[text()='Advertiser - Home']",
        "advertiser_platform":"//section//*[text()='MIF ADVERTISER PLATFORM']",
        "publisher_platform":"//section//*[text()='MIF PUBLISHER PLATFORM']",
        "Advertiser_Admin_To_Do":"//div[@class='advertisers-btn']//*[contains(text(), 'Advertiser Admin To-Do')]",
        "list_search_advertiser":"//div[@class='container-fluid']//*[text()='List / Search Advertiser']",
        "add_new_advertiser":"//div[@class='container-fluid']//*[text()='Add New Advertiser']",
        "Add_New_Advertisers_page_title":"//title[text()='Add New Advertisers']",
        "add_brand_btn":"//div[@class='container-fluid']//*[text()='Add Brand']",
        "Email_Address":"//input[@type='email']",
        "Company_site_url":"//input[@formcontrolname='site_url']",
        "First_Name":"//input[@formcontrolname='user_first_name']",
        "last_name":"//input[@formcontrolname='user_last_name']",
        "companyName":"//input[@ng-reflect-name='advertiser_name']",
        
        "primary_contact_name":"//input[@formcontrolname='primary_contact_name']",
        "primary_contact_email":"//input[@formcontrolname='primary_contact_email']",
        "primary_address_1":"//div[@formgroupname='primary_contact_address']//input[@*='address_1']",
        "primary_address_2":"//div[@formgroupname='primary_contact_address']//input[@*='address_2']",
        "primary_city":"//div[@formgroupname='primary_contact_address']//input[@*='city']",
        "primary_zipcode":"//div[@formgroupname='primary_contact_address']//input[@*='zipcode']",
        "primary_state":"//div[@formgroupname='primary_contact_address']//input[@*='state']",
        "primary_province":"//div[@formgroupname='primary_contact_address']//input[@*='province']",
        "primary_country":"//div[@formgroupname='primary_contact_address']//select[@*='country']",
        "primary_US_country":"//div[@formgroupname='primary_contact_address']//*[text()=' United States ']",

        "secondary1_contact_name":"//input[@formcontrolname='sec1_contact_name']",
        "secondary1_contact_email":"//input[@formcontrolname='sec1_contact_email']",
        "secondary1_address_1":"//div[@formgroupname='sec1_contact_address']//input[@*='address_1']",
        "secondary1_address_2":"//div[@formgroupname='sec1_contact_address']//input[@*='address_2']",
        "secondary1_city":"//div[@formgroupname='sec1_contact_address']//input[@*='city']",
        "secondary1_zipcode":"//div[@formgroupname='sec1_contact_address']//input[@*='zipcode']",
        "secondary1_state":"//div[@formgroupname='sec1_contact_address']//input[@*='state']",
        "secondary1_province":"//div[@formgroupname='sec1_contact_address']//input[@*='province']",
        "secondary1_country":"//div[@formgroupname='sec1_contact_address']//select[@*='country']",
        "secondary1_US_country":"//div[@formgroupname='sec1_contact_address']//*[text()=' United States ']",

        "secondary2_contact_name":"//input[@formcontrolname='sec2_contact_name']",
        "secondary2_contact_email":"//input[@formcontrolname='sec2_contact_email']",
        "secondary2_address_1":"//div[@formgroupname='sec2_contact_address']//input[@*='address_1']",
        "secondary2_address_2":"//div[@formgroupname='sec2_contact_address']//input[@*='address_2']",
        "secondary2_city":"//div[@formgroupname='sec2_contact_address']//input[@*='city']",
        "secondary2_zipcode":"//div[@formgroupname='sec2_contact_address']//input[@*='zipcode']",
        "secondary2_state":"//div[@formgroupname='sec2_contact_address']//input[@*='state']",
        "secondary2_province":"//div[@formgroupname='sec2_contact_address']//input[@*='province']",
        "secondary2_country":"//div[@formgroupname='sec2_contact_address']//select[@*='country']",
        "secondary2_US_country":"//div[@formgroupname='sec2_contact_address']//*[text()=' United States ']",
        "submit_button":"//button[contains(text(), 'Submit')]",
        "Advertiser_created_close_button":"//button[text()=' Close ']",
        "app-navigation":"//section[@class='main-content']//app-navigation",
        "advertiser_home_app_navig":"//app-navigation//a[text()='Advertiser Home']",
        
    }

    def _is_current_page(self):
        """This function checks if the current page is the home page by verifying the presence of specific
        elements.
        :return: a boolean value, either True or False.
        """
        advertiser_home_heading = verify_element_on_load(self.locator.advertiser_home_heading,5)
        add_new_advertiser = verify_element_on_load(self.locator.add_new_advertiser, 5)
        list_search_advertiser = verify_element_on_load(self.locator.list_search_advertiser, 5)

        if advertiser_home_heading and add_new_advertiser and list_search_advertiser is True:
            print("On Admin Advertiser Home Page")
        else:
            print("Admin Advertiser Home Page is not loaded correctly")
            return False
        return True

    def user_selects_Advertiser_Admin_To_Do_option(self):        
        """User selects the option `Advertiser_Admin_To_Do` on the advertiser page
        """
        if verify_element_on_load(self._locators["Advertiser_Admin_To_Do"]):
            self.se2lib.click_element(self._locators["Advertiser_Admin_To_Do"])
        else:
            print("Advertiser_Admin_To_Do not found....")

    def user_selects_add_new_advertiser_option(self):        
        """User slects the option `add_new_advertiser` on the advertiser page
        """
        if verify_element_on_load(self._locators["add_new_advertiser"]):
            self.se2lib.click_element(self._locators["add_new_advertiser"])
        else:
            print("add_new_advertiser not found....")

    def user_selects_list_search_advertiser_option(self):        
        """User slects the option `list_search_advertiser` on the advertiser page
        """
        if verify_element_on_load(self._locators["list_search_advertiser"]):
            self.se2lib.click_element(self._locators["list_search_advertiser"])
        else:
            print("list_search_advertiser not found....")

    def user_click_on_home_app_navigation(self):
        """ The function checks if the app navigation element is loaded and then clicks on the advertiser home
        app navigation element.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            verify_element_and_click(self._locators["advertiser_home_app_navig"])
        else:
            raise Exception

    def user_enter_email_Address(self,data):
        """ The function `user_enter_email_Address` checks if the email address field is displayed and if so,
        enters the provided data into it.
        """
        if verify_element_on_load(self.locator.Email_Address, 5) is True:
                self.se2lib.input_text(self._locators["Email_Address"], data)
        else:
            print("Email_Address is not displayed...")

    def user_enter_company_site_url(self,data):
        """ The function `user_enter_company_site_url` checks if the element with the locator `Company_site_url`
        is displayed and if so, inputs the provided data into it. If the element is not displayed, it prints
        a message.
        """
        if verify_element_on_load(self.locator.Company_site_url, 5) is True:
                self.se2lib.input_text(self._locators["Company_site_url"], data)
        else:
            print("Company_site_url is not displayed...")

    def user_enter_first_Name(self,data):
        """ The function `user_enter_first_Name` inputs the provided data into the "First_Name" field if it is
        displayed, otherwise it prints a message indicating that the field is not displayed.
        """
        if verify_element_on_load(self.locator.First_Name, 5) is True:
                self.se2lib.input_text(self._locators["First_Name"], data)
        else:
            print("First_Name is not displayed...")

    def user_enter_last_name(self,data):
        """ The function `user_enter_last_name` inputs the provided data into the "last_name" field if it is
        displayed, otherwise it prints a message indicating that the field is not displayed.
        """
        if verify_element_on_load(self.locator.last_name, 5) is True:
                self.se2lib.input_text(self._locators["last_name"], data)
        else:
            print("last_name is not displayed...")

    def user_enter_company_name(self,data):
        """ The function `user_enter_company_name` checks if the element with the locator `companyName` is
        displayed and if so, inputs the provided data into it. If the element is not displayed, it prints a
        message.
        """
        if verify_element_on_load(self.locator.companyName, 5) is True:
                self.se2lib.input_text(self._locators["companyName"], data)
        else:
            print("companyName is not displayed...")

    def user_enter_contact_name_for_Primary(self, data):
        """ The function `user_enter_contact_name` takes in a  data as parameters and inputs the data
        into the corresponding contact name field based on the field parameter.
        """
        if verify_element_on_load(self.locator.primary_contact_name, 5) is True:
            self.se2lib.input_text(self._locators["primary_contact_name"], data)
        else:
            print("primary_contact_name is not displayed...")
            raise Exception

    def user_enter_contact_name_for_secondary1(self, data):
        """ The function `user_enter_contact_name` takes in a data as parameters and inputs the data
        into the corresponding contact name field based on the field parameter.
        """
        if verify_element_on_load(self.locator.secondary1_contact_name, 5) is True:
            self.se2lib.input_text(self._locators["secondary1_contact_name"], data)
        else:
            print("secondary1_contact_name is not displayed...")
            raise Exception

    def user_enter_contact_name_for_secondary2(self, data):
        """ The function `user_enter_contact_name` takes in a data as parameters and inputs the data
        into the corresponding contact name field based on the field parameter.
        """
        if verify_element_on_load(self.locator.secondary2_contact_name, 5) is True:
            self.se2lib.input_text(self._locators["secondary2_contact_name"], data)
        else:
            print("secondary2_contact_name is not displayed...")
            raise Exception

    def user_enter_contact_email_for_Primary(self, data):
        """ The function `user_enter_contact_email` is used to enter contact email data into different fields
        based on the value of the `field` parameter.
        """
        if verify_element_on_load(self.locator.primary_contact_email, 5) is True:
            self.se2lib.input_text(self._locators["primary_contact_email"], data)
        else:
            print("primary_contact_email is not displayed...")
            raise Exception

    def user_enter_contact_email_for_secondary1(self, data):
        """ The function `user_enter_contact_email` is used to enter contact email data into different fields
        based on the value of the `field` parameter.
        """
        if verify_element_on_load(self.locator.secondary1_contact_email, 5) is True:
             self.se2lib.input_text(self._locators["secondary1_contact_email"], data)
        else:
            print("secondary1_contact_email is not displayed...")
            raise Exception

    def user_enter_contact_email_for_secondary2(self, data):
        """ The function `user_enter_contact_email` is used to enter contact email data into different fields
        based on the value of the `field` parameter.
        """
        if verify_element_on_load(self.locator.secondary2_contact_email, 5) is True:
            self.se2lib.input_text(self._locators["secondary2_contact_email"], data)
        else:
            print("secondary2_contact_email is not displayed...")
            raise Exception
    
    def user_enter_primary_address(self, data):
        """ The function `user_enter_address_1` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.primary_address_1, 5) is True:
                self.se2lib.input_text(self._locators["primary_address_1"], data)
        else:
            print("primary_address is not displayed...")
            raise Exception
   
    def user_enter_secondary1_address_1(self, data):
        """ The function `user_enter_address_1` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_address_1, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_address_1"], data)
        else:
            print("secondary1_address is not displayed...")
            raise Exception

    def user_enter_secondary2_address_1(self, data):
        """ The function `user_enter_address_1` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary2_address_1, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_address_1"], data)
        else:
            print("secondary2_address is not displayed...")
            raise Exception

    def user_enter_primary_address_2(self, data):
        """ The function `user_enter_address_2` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.primary_address_2, 5) is True:
                self.se2lib.input_text(self._locators["primary_address_2"], data)
        else:
            print("primary_address is not displayed...")
            raise Exception
        
    def user_enter_secondary1_address_2(self, data):
        """ The function `user_enter_address_2` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_address_2, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_address_2"], data)
        else:
            print("secondary1_address_2 is not displayed...")
            raise Exception

    def user_enter_secondary2_address_2(self, data):
        """ The function `user_enter_address_2` takes in a data as parameters and enters the data into
        the corresponding address field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary2_address_2, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_address_2"], data)
        else:
            print("secondary2_address_2 is not displayed...")
            raise Exception
        
    def user_enter_primary_city(self, data):
        """ The function `user_enter_city` takes in a data as parameters and inputs the data into
        the corresponding city field if the field is displayed.
        """
        if verify_element_on_load(self.locator.primary_city, 5) is True:
                self.se2lib.input_text(self._locators["primary_city"], data)
        else:
            print("primary_city is not displayed...")
            raise Exception
        
    def user_enter_secondary1_city(self, data):
        """ The function `user_enter_city` takes in a data as parameters and inputs the data into
        the corresponding city field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_city, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_city"], data)
        else:
            print("secondary1_city is not displayed...")
            raise Exception
        
    def user_enter_secondary2_city(self, data):
        """ The function `user_enter_city` takes in a data as parameters and inputs the data into
        the corresponding city field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary2_city, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_city"], data)
        else:
            print("secondary2_city is not displayed...")
            raise Exception
        
    def user_enter_primary_zipcode(self, data):
        """ The function `user_enter_zipcode` takes in a data as parameters and enters the data into
        the corresponding zipcode field if it is displayed.
        """
        if verify_element_on_load(self.locator.primary_zipcode, 5) is True:
                self.se2lib.input_text(self._locators["primary_zipcode"], data)
        else:
            print("primary_zipcode is not displayed...")
            raise Exception
        
    def user_enter_secondary1_zipcode(self,data):
        """ The function `user_enter_zipcode` takes in a data as parameters and enters the data into
        the corresponding zipcode field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_zipcode, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_zipcode"], data)
        else:
            print("secondary1_zipcode is not displayed...")
            raise Exception
        
    def user_enter_secondary2_zipcode(self, data):
        """ The function `zipcode` takes in a data as parameters and enters the data into
        the corresponding zipcode field if it is displayed.
        """
        if verify_element_on_load(self.locator.secondary2_zipcode, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_zipcode"], data)
        else:
            print("zipcode is not displayed...")
            raise Exception
    
    def user_enter_primary_state(self, data):
        """ The function `user_enter_state` takes in a data as parameters and inputs the data into the
        corresponding state field if the field is displayed.
        """
        if verify_element_on_load(self.locator.primary_state, 5) is True:
                self.se2lib.input_text(self._locators["primary_state"], data)
        else:
            print("primary_state is not displayed...")
            raise Exception
    
    def user_enter_secondary1_state(self, data):
        """ The function `user_enter_state` takes in a data as parameters and inputs the data into the
        corresponding state field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_state, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_state"], data)
        else:
            print("secondary1_state is not displayed...")
            raise Exception
        
    def user_enter_secondary2_state(self, data):
        """ The function `user_enter_state` takes in a data as parameters and inputs the data into the
        corresponding state field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary2_state, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_state"], data)
        else:
            print("secondary2_state is not displayed...")
            raise Exception
        
    def user_enter_primary_province(self, data):
        """ The function `user_enter_province` takes in a data as parameters and inputs the data into
        the corresponding province field if the field is displayed.
        """
        if verify_element_on_load(self.locator.primary_province, 5) is True:
                self.se2lib.input_text(self._locators["primary_province"], data)
        else:
            print("primary_province is not displayed...")
            raise Exception
        
    def user_enter_secondary1_province(self, data):
        """ The function `user_enter_province` takes in a data as parameters and inputs the data into
        the corresponding province field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_province, 5) is True:
                self.se2lib.input_text(self._locators["secondary1_province"], data)
        else:
            print("secondary1_province is not displayed...")
            raise Exception
        
    def user_enter_secondary2_province(self,data):
        """ The function `user_enter_province` takes in a data as parameters and inputs the data into
        the corresponding province field if the field is displayed.
        """
        if verify_element_on_load(self.locator.secondary1_province, 5) is True:
                self.se2lib.input_text(self._locators["secondary2_province"], data)
        else:
            print("secondary2_province is not displayed...")
            raise Exception
        
    def user_enter_primary_country(self, data):
        """ The function `user_enter_country` selects a country based on the provided data.
        """
        Scroll_to_element(self.locator.primary_country,250)
        if verify_element_on_load(self._locators["primary_country"],10):
                self.se2lib.click_element(self._locators["primary_country"])
                verify_element_and_click(self._locators["primary_US_country"])
        else:
            print("primary_country is not displayed...")
            raise Exception
    
    def user_enter_secondary1_country(self, data):
        """ The function `user_enter_country` selects a country based on the provided data.
        """
        Scroll_to_element(self.locator.secondary1_country,250)
        if verify_element_on_load(self._locators["secondary1_country"]):
                self.se2lib.click_element(self._locators["secondary1_country"])            
                verify_element_and_click(self._locators["secondary1_US_country"])
        else:
            print("secondary1_country is not displayed...")
            raise Exception
        
    def user_enter_secondary2_country(self, data):
        """ The function `user_enter_country` selects a country based on the provided data.
        """
        Scroll_to_element(self.locator.secondary2_country,250)
        if verify_element_on_load(self._locators["secondary2_country"]):
                self.se2lib.click_element(self._locators["secondary2_country"])                
                verify_element_and_click(self._locators["secondary2_US_country"])
        else:
            print("secondary2_country is not displayed...")
            raise Exception

    def user_click_on_submit_add_advertiser_button(self):
        """ This function clicks on the submit button for adding an advertiser if it is displayed, otherwise it
        prints a message.
        """
        if verify_element_on_load(self.locator.submit_button, 5) is True:
            Scroll_to_element(self.locator.submit_button,100)
            self.se2lib.click_element(self._locators["submit_button"])
        else:
            print("submit_button is not displayed...")
    
    def user_click_on_Advertiser_created_close_button(self):
        """ This function checks if the "Advertiser_created_close_button" element is displayed and clicks on it
        if it is, otherwise it prints a message.
        """
        if verify_element_on_load(self.locator.Advertiser_created_close_button, 5) is True:
            self.se2lib.click_element(self._locators["Advertiser_created_close_button"])
        else:
            print("Advertiser_created_close_button is not displayed...")