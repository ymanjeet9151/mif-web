from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time


class ContractFinancialTerms(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {

        "contracts_financial_page_app_navig_active":"//app-navigation//a[@class='active']/..//a[text()='Contract/Financial Terms']",
        "contracts_financial_page_heading":"//h2[contains(@class, 'display')]/..//h2[text()='Contracts/Financial Terms List']",
        "serach_by_contract_name_search_box" : "//input[@placeholder='Search By Contract Name']",
        "search_button" : "//button[text()=' Search ']",
        "reset_button" : "//button[text()=' Reset ']",
        "app-navigation":"//section[@class='main-content']//app-navigation",
        "contract_financial_app_navig":"//app-navigation//a[text()='Contract/Financial Terms']",
        "create_contract_financial_terms_button" : "//a[text()='Create Contract/Financial Terms']",

        "create_contract_financial_terms_name" : "//input[@formcontrolname='name']",
        "create_contract_financial_terms_desc" : "//textarea[@formcontrolname='description']",
        "contract_start_date" : "//input[@formcontrolname='contract_effective_date']",
        "start_date_enabled":"//div[@class='bs-datepicker-body']//span[@class='ng-star-inserted']",
        "contract_end_date" : "//input[@formcontrolname='contract_end_date']",
        "payment_terms_button": "//select[@formcontrolname='payment_terms']",
        "payment_terms_monthly" : "//select[@formcontrolname='payment_terms']/option[text()=' Monthly ']",
        "payment_terms_quartly" : "//select[@formcontrolname='payment_terms']/option[text()=' Quarterly ']",
        "reporting_cycle_button":"//select[@formcontrolname='reporting_cycle']",
        "reporting_cycle_weekly" : "//select[@formcontrolname='reporting_cycle']/option[text()=' Weekly ']",
        "reporting_cycle_monthly" : "//select[@formcontrolname='reporting_cycle']/option[text()=' Monthly ']",
        "reporting_cycle_quartly" : "//select[@formcontrolname='reporting_cycle']/option[text()=' Quarterly ']",
        "currency_code" : "//select[@formcontrolname='currency_code']/option[text()=' USD ']",
        
        "add_product_list_box":"//div[contains(@class, 'list-row')]",
        "add_product_button" : "//a[text()='Add Product']",
        "product_name_popup":"//div[@class='modal-body']//input[@formcontrolname='name']",
        "product_category_button":"//div[@class='modal-body']//input[@formcontrolname='category']",
        "product_category_popup":"//div[@class='select-dropdown ng-star-inserted']",
        "product_category_popup_option":"//a[text()='Channel Strips']",
        "product_brand_popup":"//div[@class='modal-body']//input[@formcontrolname='brand']",
        "product_brand_popup_option":"//a[text()='Samsung galaxy max']",
        "product_tagline_popup":"//div[@class='modal-body']//input[@formcontrolname='tagline']",
        "product_tags_popup":"//div[@class='modal-body']//input[@formcontrolname='tags']",
        "product_origin_country_popup":"//div[@class='modal-body']//select[@formcontrolname='countryOrigin']",
        "origin_country_us":"//option[text()=' United States ']",

        "product_name_textbox" : "//input[@formcontrolname='product_name']",
        "product_name_textbox_option":"//input[@formcontrolname='product_name']//..//a[text()='leverage interactive action-items']",
        "product_category_textbox" : "//input[@formcontrolname='product_category']",
        "product_start_date" : "//input[@formcontrolname='start_date']",
        "product_end_date" : "//input[@formcontrolname='end_date']",
        "adv_pricing_model" : "//select[@formcontrolname='pricing_modal']",
        "adv_pricing_model_option": "//option[text()=' Cost Per Action (CPA - Generic) ']",
        "adv_pricing_model_amount" : "//input[@formcontrolname='pricing_modal_amount']",
        "adv_min_spend_amount" : "//input[@formcontrolname='spend_limit_amount']",
        "spend_limit_type":"//select[@formcontrolname='spend_limit_type']",
        "spend_limit_type_weekly" : "//select[@formcontrolname='spend_limit_type']/option[text()=' Weekly ']",
        "spend_limit_type_monthly" : "//select[@formcontrolname='spend_limit_type']/option[text()=' Monthly ']",
        "spend_limit_type_yearly" : "//select[@formcontrolname='spend_limit_type']/option[text()=' Yearly ']",
        "no_of_periods":"//input[@formcontrolname='number_of_periods']",
        "unit_cost_type" : "//select[@formcontrolname='unit_cost_type']/option[text()=' Email Offer Delivery ']",
        "unit_cost_type_option":"//select[@formcontrolname='unit_cost_type']/option[text()=' Email Offer Delivery ']",
        "unit_cost_amount" : "//input[@formcontrolname='unit_cost_amount']",
        "cancel_button" : "//button[text()=' Cancel ']",

        "edit_contract_button":"//td[contains(@class,'action-btn')]//*[@class='edit-ico']",
        "update_contracts_heading":"//h2[text()=' Update Contracts/Financial Terms ']",
        "confirm_save_contract":"//button[text()=' Confirm & Save ']",
        "view_icon_contract":"//*[contains(@class,'action-btn')]//a",
        "contract_approve_button":"//button[text()=' Approve and Activate ']",
        "text_active":"//td[text()=' ACTIVE ']",
    
    }



    def _is_current_page(self):
        """
        This function checks if the current page is the Contract & Financial Page by verifying the presence of specific
        elements.
        """
        contracts_financial_page_heading = verify_element_on_load(self.locator.contracts_financial_page_heading,5)
        contracts_financial_page_app_navig_active = verify_element_on_load(self.locator.contracts_financial_page_app_navig_active, 5)

        if contracts_financial_page_heading and contracts_financial_page_app_navig_active is True:
            print("On Contract & Financial Page")
        else:
            print("Contract & Financial Page is not loaded correctly")
            return False
        return True

    def user_click_on_contract_financial_terms_app_navig(self):
        """ The function checks if a specific element is present on the page and clicks on a button if it is,
        otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            verify_element_and_click(self._locators["contract_financial_app_navig"])
        else:
            raise Exception
        
    def user_click_on_create_contract_financial_terms(self):
        """ The function checks if a specific element is present on the page and clicks on a button if it is,
        otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["create_contract_financial_terms_button"],10):
            verify_element_and_click(self._locators["create_contract_financial_terms_button"])
        else:
            raise Exception
        
    def user_enter_contract_financial_name(self, data):
        """ The function `user_enter_contract_financial_name` inputs the `data` into the
        "create_contract_financial_terms_name" field if it is displayed, otherwise it prints a message
        indicating that the field is not displayed.
        """
        if verify_element_on_load(self.locator.create_contract_financial_terms_name, 5) is True:
             self.se2lib.input_text(self._locators["create_contract_financial_terms_name"], data)
        else:
              print("contract_financial_name is not displayed...")

    def user_enter_contract_financial_terms_desc(self, data):
        """ The function `user_enter_contract_financial_terms_desc` inputs the `data` into the
        "create_contract_financial_terms_desc" field if it is displayed, otherwise it prints an error
        message.
        """
        if verify_element_on_load(self.locator.create_contract_financial_terms_desc, 5) is True:
             self.se2lib.input_text(self._locators["create_contract_financial_terms_desc"], data)
        else:
              print("contract_financial_name is not displayed...")

    def user_selects_the_current_date(self,data):
        """The function selects the current date from a calendar widget.
        """
        verify_element_on_load(self.locator.contract_start_date,10)
        Scroll_to_element(self.locator.contract_start_date, 200)
        verify_element_and_click(self.locator.contract_start_date, 10)
        time.sleep(3)
        mon_enabled_dates = self.se2lib.driver.find_element(By.XPATH, self.locator.start_date_enabled)
        mon_enabled_dates.click()
        print(mon_enabled_dates)
        
        # for dateelemnt in mon_enabled_dates:
        #     date =dateelemnt.text
        #     print(date)
        #     if date==data:
        #         dateelemnt.click()
        #         break

    def user_selects_contract_payment_term(self, option):
        """ The function allows the user to select a contract payment term option.
        """
        verify_element_and_click(self._locators["payment_terms_button"],3)
        if option=="Monthly":
            self.se2lib.click_element(self._locators["payment_terms_monthly"])
        elif option=="Quarterly":
            self.se2lib.click_element(self._locators["payment_terms_quartly"])
        else:
            print("contract_payment_term is not displayed...")
    
    def user_selects_contract_reporting_cycle(self, option):
        """ The function allows the user to select a reporting cycle option (weekly, monthly, or quarterly) and
        performs the corresponding action.
        """
        verify_element_and_click(self._locators["reporting_cycle_button"],3)
        verify_element_on_load(self._locators["reporting_cycle_weekly"])
        if option=="Weekly":
            self.se2lib.click_element(self._locators["reporting_cycle_weekly"])
        elif option=="Monthly":
            self.se2lib.click_element(self._locators["reporting_cycle_monthly"])
        elif option=="Quarterly":
            self.se2lib.click_element(self._locators["reporting_cycle_quartly"])
        else:
            print("reporting_cycle_options is not displayed...")
    
    def user_click_on_add_product_button(self):
        """The function checks if the "add_product_button" element is displayed and clicks on it, scrolling
        to the element if necessary. If the element is not displayed, it raises an exception.
        """
        if verify_element_on_load(self._locators["add_product_button"]):
            Scroll_to_element(self._locators["add_product_button"],150)
            verify_element_and_click(self._locators["add_product_button"])
        else : 
            print("add_product_button is not displayed......")
            raise Exception

    def user_enter_product_name(self,data):
        """ The function `user_enter_product_name` takes in a data dictionary and inputs the product name into a
        popup if it is displayed, otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["product_name_popup"]):
            self.se2lib.input_text(self._locators["product_name_popup"], data["name"])
        else : 
            print("product_name_popup is not displayed......")
            raise Exception

    def user_enter_product_category(self,data):
        """ The function `user_enter_product_category` takes in a data dictionary as input and enters the
        product category into a text field, then selects the corresponding option from a popup menu. If the
        product category button is not displayed, an exception is raised.
        """
        if verify_element_on_load(self._locators["product_category_button"]):
            self.se2lib.input_text(self._locators["product_category_button"], data["product_category"])
            verify_element_and_click(self._locators["product_category_popup_option"], 5)
        else : 
            print("product_category is not displayed......")
            raise Exception

    def user_enter_product_brand(self,data):
        """The function `user_enter_product_brand` inputs the product brand into a popup and selects an option
        from the popup if it is displayed, otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["product_brand_popup"]):
            self.se2lib.input_text(self._locators["product_brand_popup"], data["brand"])
            verify_element_and_click(self._locators["product_brand_popup_option"],5)
        else : 
            print("product_category is not displayed......")
            raise Exception
        
    def user_enter_product_tagline(self,data):
        """ The function `user_enter_product_tagline` takes in a data dictionary as input and enters the
        tagline value into the product tagline field if the product name popup is displayed. If the
        product name popup is not displayed, it raises an exception.
        """
        if verify_element_on_load(self._locators["product_name_popup"]):
            self.se2lib.input_text(self._locators["product_tagline_popup"], data["tagline"])
        else : 
            print("product_name_popup is not displayed......")
            raise Exception
        
    def user_enter_product_tags(self,data):
        """The function `user_enter_product_tags` takes in a data dictionary and inputs the tags into a
        product tags popup if it is displayed, otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["product_tags_popup"]):
            self.se2lib.input_text(self._locators["product_tags_popup"], data["tags"])
        else : 
            print("product_tags_popup is not displayed......")
            raise Exception
        
    def user_selects_the_country(self):
        """ The function checks if a product origin country popup is displayed, and if so, the user selects the
        US as the origin country. If the popup is not displayed, an exception is raised.
        """
        if verify_element_on_load(self._locators["product_origin_country_popup"]):
            self.se2lib.click_element(self._locators["product_origin_country_popup"])
            verify_element_and_click(self._locators["origin_country_us"])
        else : 
            print("product_origin_country_popup is not displayed......")
            raise Exception

    def user_select_the_product(self):
        """The function `user_select_the_product` selects a product from a dropdown menu if the product name
        textbox is displayed, otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["product_name_textbox"]):
            verify_element_and_click(self._locators["product_name_textbox"])
            self.se2lib.click_element(self._locators["product_name_textbox_option"])
        else : 
            print("product_name_textbox is not displayed......")
            raise Exception

    def user_enter_pricing_model(self):
        """The function checks if the "adv_pricing_model" element is displayed, and if so,
        clicks on it and selects the "adv_pricing_model_option" element, otherwise it prints an error
        message and raises an exception.
        """
        if verify_element_on_load(self._locators["adv_pricing_model"],10) is True:
            self.se2lib.click_element(self._locators["adv_pricing_model"])
            self.se2lib.click_element(self._locators["adv_pricing_model_option"])
            time.sleep(3)
        else : 
            print("adv pricing model is not displayed......")
            raise Exception

    def user_enter_adv_pricing_model_amount(self,data):
        """ The function `user_enter_adv_pricing_model_amount` inputs a value into the
        "adv_pricing_model_amount" field if it is displayed, otherwise it prints a message.
        """
        verify_element_on_load(self.locator.add_product_list_box, 25)
        table_box = self.se2lib.driver.find_element(By.XPATH, self.locator.add_product_list_box)
        self.se2lib.driver.execute_script("arguments[0].scrollLeft = 250;", table_box)

        if verify_element_on_load(self.locator.adv_pricing_model_amount) is True:
            self.se2lib.input_text(self._locators["adv_pricing_model_amount"], data["adv_pricing_model_amount"])
            time.sleep(5)
        else : 
            print("adv pricing model amount is not displayed......")

    def user_enter_adv_min_spend_amount(self,data):
        """The function checks if the "adv_min_spend_amount" element is displayed and if so, it inputs the
        value from the "data" dictionary into the element. If the element is not displayed, it prints a
        message.
        """
        if verify_element_on_load(self.locator.adv_min_spend_amount) is True:
            self.se2lib.input_text(self._locators["adv_min_spend_amount"], data["adv_min_spend_amount"])
        else : 
            print("adv min spend amount is not displayed......")

    def user_enter_spend_limit_type(self):
        """The function checks if the spend limit type element is displayed and selects the yearly option if it
        is, otherwise it prints an error message.
        """
        if verify_element_on_load(self.locator.spend_limit_type) is True:
            self.se2lib.click_element(self._locators["spend_limit_type"])
            self.se2lib.click_element(self._locators["spend_limit_type_yearly"])
        else : 
            print("spend_limit_type is not displayed......")

    def user_enter_number_of_periods(self,data):
        """ The function checks if the "no_of_periods" element is displayed and if so, it inputs the
        user-entered number of periods into the element. If the element is not displayed, it prints a
        message.
        """
        if verify_element_on_load(self.locator.no_of_periods) is True:
            self.se2lib.input_text(self._locators["no_of_periods"], data["number_of_periods"])
        else :
            print("no_of_periods is not displayed......")

    def user_enter_unit_cost_type(self):
        """The function checks if the unit_cost_type element is displayed, and if so, clicks on it and selects
        an option. If the element is not displayed, it prints a message.
        """
        if verify_element_on_load(self.locator.unit_cost_type) is True:
            self.se2lib.click_element(self._locators["unit_cost_type"])
            self.se2lib.click_element(self._locators["unit_cost_type_option"])
        else : 
            print("unit_cost_type is not displayed......")
    
    def user_enter_unit_cost_amount(self,data):
        """ The function checks if the unit_cost_amount element is displayed and if so, it inputs the provided
        data into the element. If the element is not displayed, it prints a message.
        """
        if verify_element_on_load(self.locator.unit_cost_amount) is True:
            self.se2lib.input_text(self._locators["unit_cost_amount"], data["unit_cost_amount"])
        else :
            print("unit_cost_amount is not displayed......")

    def user_confirm_save_the_contract(self):
        """ The function checks if the "edit_contract_button" is displayed, and if so, it clicks on it, waits
        for the "update_contracts_heading" element to be visible, scrolls to the "confirm_save_contract"
        element, and clicks on it; otherwise, it prints an error message and raises an exception.
        """
        if verify_element_on_load(self.locator.edit_contract_button,7) is True:
            self.se2lib.click_element(self.locator.edit_contract_button)
            wait = WebDriverWait(self.se2lib.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.locator.update_contracts_heading)))
            Scroll_to_element(self.locator.confirm_save_contract)
            verify_element_and_click(self._locators["confirm_save_contract"])
        else :
            print("Confirm_Save button is not displayed......")
            raise Exception

    def user_approve_the_contract(self):
        """ The function `user_approve_the_contract` verifies if the contract view icon is displayed, clicks on
        it, scrolls to the contract approve button, clicks on it, and checks if the text "ACTIVE" is
        displayed. If the contract view icon is not displayed, it raises an exception.
        """
        if verify_element_on_load(self.locator.view_icon_contract,5) is True:
            self.se2lib.click_element(self.locator.view_icon_contract)
            time.sleep(3)
            Scroll_to_element(self.locator.contract_approve_button)
            self.se2lib.click_element(self.locator.contract_approve_button)
            time.sleep(2)
            "ACTIVE"==self.se2lib.get_text(self._locators["text_active"])
        else :
            print("Approve_the_contract is not displayed......")
            raise Exception
