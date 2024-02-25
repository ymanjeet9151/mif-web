from robot.libraries.BuiltIn import BuiltIn
from PageObjectLibrary import PageObject
from utils.generic_keywords import *
from modules.custom_keywords import *
from selenium.webdriver.common.by import By
import time


class ProductOfferAd(PageObject):
    """
    WebElements and keywords for Home Page.
    """
    _locators = {

        "serach_by_contract_name_search_box" : "//input[@placeholder='Search By Contract Name']",
        "search_button" : "//button[text()=' Search ']",
        "reset_button" : "//button[text()=' Reset ']",
        "app-navigation":"//section[@class='main-content']//app-navigation",
        "advertiser_home_app_navig":"//app-navigation//a[text()='Advertiser Home']",        
        "Advertiser_List_app_navig":"//app-navigation//a[text()='Advertiser List']",
        "create_contract_financial_terms_button" : "//a[text()='Create Contract/Financial Terms']",
        "Product_Offer_Ads_app_navig":"//app-navigation//a[text()='Product Offer Ads/Assets']",
        "Product_Offer_Ads_app_navig_heading":"//h2[contains(@class, 'display')]/..//h2[text()='Product Offer Ads/Assets List']",
        "Product_Offer_Ads_app_navig_active":"//app-navigation//a[@class='active']/..//a[text()='Product Offer Ads/Assets']",

        "product_offer_ads_assets_tab" : "//a[text()='Product Offer Ads/Assets']",
        "add_offer_button":"//a[text()=' Add Offer']",
        "add_offer_product_name" : "//select[@formcontrolname='productName']",
        "offer_name" : "//input[@formcontrolname='offerName']",
        "ad_type_button":"//select[@formcontrolname='adType']",
        "ad_type_email_offer" : "//select[@formcontrolname='adType']/option[@value='EMAIL_OFFER']",
        "ad_type_actionable_display" : "//select[@formcontrolname='adType']/option[@value='ACTIONABLE_DISPLAY']",
        "ad_type_display" : "//select[@formcontrolname='adType']/option[@value='DISPLAY']",
        "ad_offer_description" : "//textarea[@formcontrolname='description']",
        "offer_expiration_date" : "//input[@formcontrolname='offerExpirationDate']",

        "add_assets_form":"//div[@class='modal-body']//h2[text()= 'Add Assets']",
        "add_assets_button" : "//a[text()= ' Add Assets']",
        "asset_type_button":"//select[@formcontrolname='assetType']",
        "asset_type_offer_logo" : "//select[@formcontrolname='assetType']/option[text()=' Offer Logo ']",
        "asset_type_email_offer_image" : "//select[@formcontrolname='assetType']/option[text()=' Email Offer Image ']",
        "logo_name" : "//input[@formcontrolname='logoName']",
        "asset_size" : "//select[@formcontrolname='assetSize']",
        "offer_link_destination_url" : "//input[@formcontrolname='clickLinkURL']",
        "model_click_destination_android_url" : "//input[@formcontrolname='modal_click_destination_android_url']",
        "model_fetch_logo_android_url" : "//input[@formcontrolname='modal_fetch_logo_android_url']",
        "email_offer_click_destination_android_url" : "//input[@formcontrolname='email_offer_click_destination_android_url']",
        "email_offer_text" : "//input[@formcontrolname='emailText']",
        "email_subject_line_text" : "//input[@formcontrolname='emailSubjectText']",
        "email_preview_line_text" : "//input[@formcontrolname='emailPreviewText']",
        "rewardsLinkURL":"//input[@formcontrolname='rewardsLinkURL']",
        "save_add_product_button" : "//button[@class='submit mt-0 add-product mx-3']",
        "upload_file":"//input[@id='fileSelect']",
        "save_add_offer":"//button[@class='green-btn']",

        "productOfferAds_list_table":"//div[@class='table-list table']/table",
        "switch_box_product_activation":"//div[@class='switch-box']//input[@id='checkbox_1']/..//label",
        "switch_box_product_enabled":"//input[@id='checkbox_1']/..//input[@value='true']",
        
    }



    def _is_current_page(self):
        """
        This function checks if the current page is the Advertiser Product Offer Ads Page by verifying the presence of specific
        elements.
        """
        Product_Offer_Ads_app_navig_active = verify_element_on_load(self.locator.Product_Offer_Ads_app_navig_active,5)
        Product_Offer_Ads_app_navig_heading = verify_element_on_load(self.locator.Product_Offer_Ads_app_navig_heading, 5)

        if Product_Offer_Ads_app_navig_active and Product_Offer_Ads_app_navig_heading is True:
            print("On advertiser Product Offer Ads Page")
        else:
            print("Advertiser Product Offer Ads Page is not loaded correctly")
            return False
        return True
    
    def user_click_on_product_Offer_Ads_app_navig(self):
        """ The function checks if a specific element is present on the page and clicks on it if it is,
        otherwise it raises an exception.
        """
        if verify_element_on_load(self._locators["app-navigation"],10):
            verify_element_and_click(self._locators["Product_Offer_Ads_app_navig"])
        else:
            raise Exception   

    def user_click_on_add_offer(self):
        """The function `user_click_on_add_offer` checks if the "add_offer_button" element is displayed, clicks
        on it if it is, and verifies if the "add_offer_product_name" element is loaded within 7 seconds. If
        the "add_offer_button" element is not displayed, it raises an exception.
        """
        if verify_element_on_load(self.locator.add_offer_button) is True:
            self.se2lib.click_element(self._locators["add_offer_button"])
            verify_element_on_load(self.locator.add_offer_product_name,7)
        else : 
            print("add_offer is not displayed......")
            raise Exception

    def user_enter_offer_name(self, data):
        """ The function `user_enter_offer_name` checks if the offer name element is displayed and if so, inputs
        the offer name provided in the `data` dictionary, otherwise it prints a message indicating that the
        offer name is not displayed.
        """
        if verify_element_on_load(self.locator.offer_name) is True:
            self.se2lib.input_text(self._locators["offer_name"], data["offer_name"])
        else : 
            print("offer_name is not displayed......")
    
    def user_selects_ad_type(self, data):
        """The function `user_selects_ad_type` allows the user to select an ad type based on the given data.
        """
        verify_element_on_load(self.locator.ad_type_button)
        self.se2lib.click_element(self._locators["ad_type_button"])
        if data =='Email Offer':
            self.se2lib.click_element(self._locators["ad_type_email_offer"])
        elif data =='Actionable Display':
            self.se2lib.click_element(self._locators["ad_type_actionable_display"])
        elif data =='Display':
            self.se2lib.click_element(self._locators["ad_type_display"])
        else : 
            print("selects_ad_type is not displayed......")

    def user_enter_description(self, data):
        """ The function `user_enter_description` checks if an element is displayed and inputs text into it if
        it is, otherwise it prints a message.
        """
        if verify_element_on_load(self.locator.ad_offer_description) is True:
            self.se2lib.input_text(self._locators["ad_offer_description"], data["ads_offer_desc"])
        else : 
            print("unit_cost_type is not displayed......")

    def user_click_on_add_assets(self):
        """ The function `user_click_on_add_assets` scrolls to the add assets button, clicks on it, and verifies
        if the add assets form is displayed. If the add assets button is not displayed, it raises an
        exception.
        """
        Scroll_to_element(self.locator.add_assets_button, 150)
        if verify_element_on_load(self.locator.add_assets_button) is True:
            self.se2lib.click_element(self._locators["add_assets_button"])
            verify_element_on_load(self.locator.add_assets_form,5)
        else : 
            print("add_offer is not displayed......")
            raise Exception
        
    def user_selects_asset_type(self, asset_type):
        """ The function `user_selects_asset_type` allows the user to select an asset type, such as "Offer Logo"
        or "Email Offer Image", and raises an exception if the asset type is not displayed.
        """
        verify_element_and_click(self._locators["asset_type_button"])
        if asset_type=='Offer Logo':
            self.se2lib.click_element(self._locators["asset_type_offer_logo"])
        elif asset_type=='Email Offer Image':
            self.se2lib.click_element(self._locators["asset_type_email_offer_image"])
        else : 
            print("asset type is not displayed......")
            raise Exception

    def user_enter_logo_name(self, data):
        """The function `user_enter_logo_name` inputs the appropriate logo name based on the data.
        """
        if verify_element_on_load(self.locator.logo_name,5):
            self.se2lib.input_text(self._locators["logo_name"], data)
        else : 
            print("logo_name is not displayed......")
            raise Exception
        
        popup_box = self.se2lib.driver.find_element(By.XPATH, self.locator.save_add_product_button)
        self.se2lib.driver.execute_script("arguments[0].scrollIntoView();", popup_box)

    def user_attach_doc_to_assets(self,file_path):
        """The function `user_attach_doc_to_assets` attaches a document to assets by choosing a file and
        printing a success message.
        """
        self.se2lib.choose_file(self.locator.upload_file,file_path)
        time.sleep(10)
        print("successfully attached the file")

    def user_click_on_assets_save_button(self):
        """The function `user_click_on_assets_save_button` clicks on the save button for adding a product if it
        is displayed, otherwise it raises an exception.
        """
        if verify_element_on_load(self.locator.save_add_product_button,10) is True:
            self.se2lib.click_element(self._locators["save_add_product_button"])
            time.sleep(5)
        else : 
            print("save_add_product_button is not displayed......")
            raise Exception

    def user_enter_offer_click_link_destination_url(self, data):
        """The function checks if an element is displayed and if so, inputs a specified URL into a text field,
        otherwise it raises an exception.
        """
        if verify_element_on_load(self.locator.offer_link_destination_url,5) is True:
            self.se2lib.input_text(self._locators["offer_link_destination_url"], data["offer_click_link_destination_url"])
        else : 
            print("offer_click_link_destination_url is not displayed......")
            raise Exception
    
    def user_enter_email_offer_text(self, data):
        """ This function enters the email offer text on the basis of given data
        """
        if verify_element_on_load(self.locator.email_offer_text,5) is True:
            self.se2lib.input_text(self._locators["email_offer_text"], data["email_offer_text"])
        else : 
            print("email_offer_text is not displayed......")
            raise Exception
        
    def user_enter_email_subject_line_text(self, data):
        """ This function enters the `email_subject_line_text` on the basis of given data
        """
        if verify_element_on_load(self.locator.email_subject_line_text,5) is True:
            self.se2lib.input_text(self._locators["email_subject_line_text"], data["email_subject_line_text"])
        else : 
            print("email_subject_line_text is not displayed......")
            raise Exception
        
    def user_enter_email_preview_line_text(self, data):
        """ The function `user_enter_email_preview_line_text` checks if the email preview line text element is
        displayed and inputs the provided data if it is, otherwise it raises an exception.
        """
        if verify_element_on_load(self.locator.email_preview_line_text,5) is True:
            self.se2lib.input_text(self._locators["email_preview_line_text"], data["email_preview_line_text"])
        else : 
            print("email_preview_line_text is not displayed......")
            raise Exception
        
    def user_enter_email_ty_rewards_clicks_link_url(self, data):
        """The function checks if the rewardsLinkURL element is displayed and if so, enters the provided data
        into the element, otherwise it raises an exception.
        """
        if verify_element_on_load(self.locator.rewardsLinkURL,5) is True:
            self.se2lib.input_text(self._locators["rewardsLinkURL"], data["rewardsLinkURL"])
        else : 
            print("rewardsLinkURL is not displayed......")
            raise Exception
        
    def user_click_on_save_add_offer_button(self):
        """ this function scroll to the element, varify and click on `save_add_offer` btn 
        """
        Scroll_to_element(self.locator.save_add_offer)
        if verify_element_on_load(self.locator.save_add_offer,5) is True:
            self.se2lib.click_element(self._locators["save_add_offer"])
            time.sleep(5)
        else : 
            print("save_add_offer is not displayed......")
            raise Exception
        
    def user_activate_the_product_offer(self):
        """ This function activate the product offer and also validate is switch_box_product enabled.
        """
        if verify_element_on_load(self._locators["productOfferAds_list_table"], 7) is True:
            table_box = self.se2lib.driver.find_element(By.XPATH, self.locator.productOfferAds_list_table)
            self.se2lib.driver.execute_script("arguments[0].scrollLeft = 520;", table_box)
            switch_box = self.se2lib.driver.find_element(By.XPATH, self.locator.switch_box_product_activation)
            self.se2lib.driver.execute_script("arguments[0].scrollIntoView();", switch_box)
            verify_element_and_click(self._locators["switch_box_product_activation"],7)
            verify_element_on_load(self._locators["switch_box_product_enabled"])
            time.sleep(3)
        else:
            raise Exception