from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Campaigns(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {

        "app-navigation":"//section[@class='main-content']//app-navigation",
        "campaign_list_heading":"//h3[contains(@class, 'display')]/..//h3[text()='Campaign List']",
        "campaigns_app_navig":"//app-navigation//a[text()='Campaigns']",
        "campaigns_app_navig_active":"//app-navigation//a[@class='active']/..//a[text()='Campaigns']",
        "campaingns_tab" : "//a[text()='Campaigns']",
        "search_textbox" : "//input[@placeholder='Search']",
        "search_green_button" : "//button[text()=' Search ']",
        "reset_button" : "//button[text()=' Reset ']",
        "create_campaign_button" : "//a[text()='Create Campaign']",
        "add_new_campaign" : "//input[@placeholder='Add New Campaign']",
        "campaign_description" : "//textarea[@formcontrolname='description']",
        "save_button" : "//a[text()='Save']",
        "next_button" : "//a[text()='Next']",
        "campaing_start_date":"//div[@class='campaings-container']//input[@formcontrolname='start_date']",
        "start_date_enabled":"//div[@class='bs-datepicker-body']//span[@class='ng-star-inserted']",
        "spend_limit_period_type":"//select[@formcontrolname='spend_limit_period_type']",
        "spend_limit_period_weekly":"//select[@formcontrolname='spend_limit_period_type']//option[text()=' Weekly ']",
        "spend_limit_period_monthly":"//select[@formcontrolname='spend_limit_period_type']//option[text()=' Monthly ']",
        "campaign_spend_limit_amt":"//input[@formcontrolname='spend_limit_amt']",

        "add_product_to_campaign":"//a[text()='Add Product to Campaign']",
        "product_name_campaign":"//select[@formcontrolname='product_name']",
        "option_product_campaign":"//select[@formcontrolname='product_name']/option[2]",
        "add_product_level_targeting_button":"//a[text()='Add Product Level Targeting']",
        "male_checkbox":"//div[@class='card card-body']//*[text()=' Male ']",
        "female_checkbox":"//div[@class='female-col']//*[text()=' Female ']",
        "add_product_offer_ad_button":"//a[text()='Add Product Offer Ad']",
        "product_offer_ad_campaign":"//select[@formcontrolname='productOffer']",
        "product_offer_ad_option":"//select[@formcontrolname='productOffer']/*[2]",
        "save_add_product_campaign":"//*[text()=' Save ']",
        "campaign_edit_button":"//td[text()=' 1 ']/..//*[@data-tooltip='Edit']",
        "add_products_campaign_arrow_btn":"//div[text()='Add Products to Campaign']",
        "confirm_save_btn":"//a[text()='Confirm & Save']",
        "commit_campaign_popup":"//h2[text()='Commit Campaign']",
        "campaign_yes_btn":"//h2[text()='Commit Campaign']/..//button[text()=' Yes ']",
        "set_financials_promotions_btn":"//a[text()=' Set Financials/Promotions ']",
        "campaign_promotion_type":"//label[text()='Campaign Promotion Type']//..//select[@*='promotion_type_id']",
        "email_count_promotion_type":"//label[text()='Campaign Promotion Type']//..//option[text()=' Email Count ']",
        "promotion_email_count":"//input[@formcontrolname='promotion_email_count']",
        "promotion_value_amount":"//input[@formcontrolname='promotion_value_amount']",
        "payment_amount_received":"//input[@formcontrolname='payment_amount_received']",
        "modal_display_priority":"//select[@formcontrolname='modal_display_priority']",
        "modal_display_priority_option":"//select[@formcontrolname='modal_display_priority']/option[2]",

        "full_campaign_view":"//a[text()='Full Campaign View']",
        "review_approve_btn":"//a[text()='Review & Approve ']",
        "campaign_approved_active_text":"//div[@class='campaings-container']//*[text()='CAMPAIGN_STATUS_APPROVED']",
        "campaign_table_list":"//div[contains(@class,'table-list table')]/table",
        "campaign_activate_switchbox":"//div[@class='switch-box']//label[@for='checkbox_campaign_0']",
        "campaign_deactivated":"//label[@for='checkbox_campaign_0']/..//input[@value='false']",
        "campaign_activate":"//label[@for='checkbox_campaign_0']/..//input[@value='true']",
    
    }



    def _is_current_page(self):
        """
        This function checks if the current page is the Campaign Page by verifying the presence of specific
        elements.
        """
        campaign_list_heading = verify_element_on_load(self.locator.campaign_list_heading,5)
        campaigns_app_navig_active = verify_element_on_load(self.locator.campaigns_app_navig_active, 5)

        if campaign_list_heading and campaigns_app_navig_active is True:
            print("On Campaign page")
        else:
            print("Campaign page is not loaded correctly")
            return False
        return True

    def user_click_on_campaigns_app_navig(self):
        """ The function checks if a specific element is loaded and then clicks on another element if it is.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            time.sleep(3)
            verify_element_and_click(self._locators["campaigns_app_navig"])
        else:
            raise Exception    

    def user_click_on_create_campaign_button(self):
 
        if verify_element_and_click(self._locators["create_campaign_button"], 7):
            print("successfully clicked on create_campaign_button")
        else:
            print("create_campaign_button is not displayed......")

    def user_enter_campaign_name(self, data):
 
        if verify_element_on_load(self.locator.add_new_campaign,5) is True:
            self.se2lib.input_text(self._locators["add_new_campaign"], data["name"])
        else : 
            print("add_new_campaign is not displayed......")
            raise Exception

    def user_enter_campaign_description(self, data):
 
        if verify_element_on_load(self.locator.campaign_description,5) is True:
            self.se2lib.input_text(self._locators["campaign_description"], data["description"])
        else : 
            print("campaign_description is not displayed......")
            raise Exception
         
    def user_click_on_next_button_campaign(self):
 
        if verify_element_on_load(self.locator.next_button,5) is True:
            Scroll_to_element(self.locator.next_button)
            self.se2lib.click_element(self._locators["next_button"])
        else : 
            print("next_button is not displayed......")
            raise Exception
        
    def user_click_on_save_button_campaign(self):
 
        if verify_element_on_load(self.locator.save_button,5) is True:
            Scroll_to_element(self.locator.save_button)
            self.se2lib.click_element(self._locators["save_button"])
        else : 
            print("save_button_campaign is not displayed......")
            raise Exception
        
    def user_selects_the_campaings_current_date(self):
        """The function selects the current date from a calendar widget.
        """
        verify_element_on_load(self.locator.campaing_start_date,10)
        Scroll_to_element(self.locator.campaing_start_date, 200)
        verify_element_and_click(self.locator.campaing_start_date, 10)
        time.sleep(3)
        mon_enabled_dates = self.se2lib.driver.find_element(By.XPATH, self.locator.start_date_enabled)
        mon_enabled_dates.click()
        print(mon_enabled_dates)

    def user_selects_campaign_spend_limit_period_type(self, data):
 
        verify_element_and_click(self.locator.spend_limit_period_type,5)
        if data =='monthly':
            verify_element_and_click(self._locators["spend_limit_period_monthly"])
        elif data =='Weekly':
            verify_element_and_click(self._locators["spend_limit_period_weekly"])
        else : 
            print("spend_limit_period_type is not displayed......")
            raise Exception
        
    def user_enters_campaign_spend_limit_amt(self, data, key):
 
        if verify_element_on_load(self.locator.campaign_spend_limit_amt,5) is True:
            self.se2lib.input_text(self._locators["campaign_spend_limit_amt"], data[key])
        else :
            print("campaign_spend_limit_amt is not displayed......")
            raise Exception

    def user_click_on_add_product_to_campaign_button(self):
 
        if verify_element_on_load(self.locator.add_product_to_campaign,5) is True:
            self.se2lib.click_element(self.locator.add_product_to_campaign)
            print("Successfully clicked on add_product_to_campaign")
        else : 
            print("add_product_to_campaign_button is not displayed......")
            raise Exception

    def user_selects_product_name_campaign(self,option_index):
 
        verify_element_and_click(self.locator.product_name_campaign,5)
        if option_index =='0':
            self.se2lib.click_element(self._locators["option_product_campaign"])
        else : 
            print("product_name_campaign is not displayed......")
            raise Exception
    
    def user_selects_product_offer_ad_campaign(self):
 
        offer_ad_button = self.se2lib.driver.find_element(By.XPATH, self.locator.add_product_offer_ad_button)
        self.se2lib.driver.execute_script("arguments[0].scrollIntoView();", offer_ad_button)
        if verify_element_on_load(self.locator.add_product_offer_ad_button,5) is True:
            verify_element_and_click(self._locators["add_product_offer_ad_button"])
            verify_element_and_click(self._locators["product_offer_ad_campaign"])
            verify_element_and_click(self._locators["product_offer_ad_option"])
        else : 
            print("product_name_dropdown is not displayed......")
            raise Exception
        
    def user_click_on_save_add_product_to_campaign(self):
 
        if verify_element_on_load(self.locator.save_add_product_campaign,5) is True:
            save_add_product = self.se2lib.driver.find_element(By.XPATH, self.locator.save_add_product_campaign)
            self.se2lib.driver.execute_script("arguments[0].scrollIntoView();", save_add_product)
            self.se2lib.click_element(self._locators["save_add_product_campaign"])
            time.sleep(5)
        else : 
            print("save_button_campaign is not displayed......")
            raise Exception
    
    def user_clicks_on_campaign_edit_btn(self):
 
        if verify_element_on_load(self.locator.campaign_edit_button,5) is True:
            self.se2lib.click_element(self.locator.campaign_edit_button)
        else : 
            print("campaign_edit_button is not displayed......")
            raise Exception
        
    def user_navigates_to_add_product_to_campagin_page(self):
 
        if verify_element_on_load(self.locator.add_products_campaign_arrow_btn,5) is True:
            self.se2lib.click_element(self.locator.add_products_campaign_arrow_btn)
            verify_element_on_load(self.locator.add_product_to_campaign,5)
        else : 
            print("add_products_campaign is not displayed......")
            raise Exception
        
    def user_save_and_confirm_campaign_product(self):
 
        if verify_element_on_load(self.locator.confirm_save_btn,5) is True:
            Scroll_to_element(self.locator.confirm_save_btn)
            self.se2lib.click_element(self.locator.confirm_save_btn)
            verify_element_on_load(self.locator.commit_campaign_popup,5)
            self.se2lib.click_element(self.locator.campaign_yes_btn)
        else : 
            print("add_products_campaign is not displayed......")
            raise Exception
        
    def user_click_on_set_financials_promotions_btn(self):
 
        if verify_element_on_load(self.locator.set_financials_promotions_btn,5) is True:
            self.se2lib.click_element(self.locator.set_financials_promotions_btn)
        else : 
            print("add_products_campaign is not displayed......")
            raise Exception
        
    def user_selects_campaign_promotion_type(self):
 
        if verify_element_on_load(self.locator.save_add_product_campaign) is True:
            save_add_product = self.se2lib.driver.find_element(By.XPATH, self.locator.save_add_product_campaign)
            self.se2lib.driver.execute_script("arguments[0].scrollIntoView();", save_add_product)
            self.se2lib.click_element(self.locator.campaign_promotion_type)
            self.se2lib.click_element(self.locator.email_count_promotion_type)
        else : 
            print("add_products_campaign is not displayed......")
            raise Exception
        
    def user_enters_promotion_email_count(self, data):
 
        if verify_element_on_load(self.locator.promotion_email_count,5) is True:
            self.se2lib.input_text(self._locators["promotion_email_count"], data["promotion_email_count"])
        else :
            print("campaign_spend_limit_amt is not displayed......")
            raise Exception
        
    def user_enters_payment_amt_received(self, data):
 
        if verify_element_on_load(self.locator.payment_amount_received,5) is True:
            self.se2lib.input_text(self._locators["payment_amount_received"], data["payment_amount_received"])
        else :
            print("campaign_spend_limit_amt is not displayed......")
            raise Exception
        
    def user_selects_modal_display_priority(self):
 
        if verify_element_on_load(self.locator.modal_display_priority) is True:
            self.se2lib.click_element(self.locator.modal_display_priority)
            self.se2lib.click_element(self.locator.modal_display_priority_option)
        else : 
            print("modal_display_priority is not displayed......")
            raise Exception
        
    def user_click_on_full_campaign_view(self):
 
        if verify_element_on_load(self.locator.full_campaign_view) is True:
            self.se2lib.click_element(self.locator.full_campaign_view)
        else : 
            print("modal_display_priority is not displayed......")
            raise Exception
        
    def user_click_on_review_and_approve_campaign(self):
 
        if verify_element_on_load(self.locator.review_approve_btn) is True:
            self.se2lib.click_element(self.locator.review_approve_btn)
        else : 
            print("review_approve_btn is not displayed......")
            raise Exception
        
    def user_validate_the_campaign_status(self,data):
 
        if verify_element_on_load(self.locator.campaign_approved_active_text) is True:
           text=self.se2lib.get_text(self._locators["campaign_approved_active_text"])
           print(text,data)
           data==text
        else : 
            print("campaign_approved_active_text is not displayed......")
            raise Exception
    
    def user_activate_the_campaign(self):
        if verify_element_on_load(self.locator.campaign_table_list) is True:
            campaign_table = self.se2lib.driver.find_element(By.XPATH, self.locator.campaign_table_list)
            self.se2lib.driver.execute_script("arguments[0].scrollLeft = 520;", campaign_table)
            verify_element_on_load(self.locator.campaign_deactivated,5)
            verify_element_and_click(self.locator.campaign_activate_switchbox)
            verify_element_on_load(self.locator.campaign_activate, 5)
        else : 
            print("add_products_campaign is not displayed......")
            raise Exception
