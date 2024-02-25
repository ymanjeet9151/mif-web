
*** Settings ***
| Documentation | MIF Generic Keywords
| Library | datadrivenlibrary.CsvLibrary
| Library | Collections
| Library | String
| Library | DateTime
| Library | random
| Variables | ../../pagelibraries/resources/config.py
| Library | ../custom_keywords.py
| Resource | utils/common.robot
| Resource | utils/generic-keywords.robot
| Resource |   utils/api-generic-keyword.robot
| Library | utils.environmentsetup
| Library  | utils/db.py
| Library  | PageObjectLibrary
| Library  | SeleniumLibrary
| Library  | Process


***Variables***
| ${pathtocsvfile} | ${CONFIG.data_file_path}
| ${host} | ${CONFIG.host}
| ${domain} | ${CONFIG.domain}
| ${endpoint} | ${CONFIG.endpoint}
| ${filename} | DataAdminAdvertiser.json

***Keywords***

| Open Browser and Load Required Page Objects
| | [Documentation] | Initiate the Suite by opening browser about:blank page
| | ... | and validate all the required pages for execution
| | Log | Loading page Objects | console=${True}
| | Close All Browsers
| | Open Test Browser | URL=${CONFIG.root_url}
| | Maximize Browser Window
| | set selenium speed | 0.8
| | Go to page | HomePage
| | Go to page | SigninPage
| | Go to page | AdminAdvertiserHome
| | Go to page | AdvertiserList
| | Go to page | ContractFinancialTerms
| | Go to page | ProductOfferAd
| | Go to page | Campaigns
| | Go to page | AdminToDoList

| Capture Screen Shots AND Close Browser
| | [Documentation] | capturing the screen shots and closing the browser
| | Capture Page Screenshot
| | Close All Browsers

| User Launch an Application
| | [Documentation] | User opens the application URL
| | [Arguments] | ${endpoint}=None | ${page}=None | ${host}=${host}
| | [Timeout] | 50s
| | Open To Application URL | ${host} | ${endpoint}
| | The Application Should Be Redirected on ${page}

| User Able to login to an Application
| | [Documentation] | User Signin with the Registered user details
| | [Arguments] | ${Email} | ${password}
| | The Application Should Be Redirected on SigninPage
| | Enter User Email | ${Email}
| | Enter User Password | ${password}
| | User Click on Signin Button
| | The Application Should Be Redirected on HomePage

| User Add New Admin advertisers
| | [Documentation] | User Expected to Add New Admin Advertiser User. 
| | [Arguments] | ${option} | ${Test}
| | User selects add new advertiser option
| | User Fill up the Advertiser details | ${Test}
| | User Click on Submit Add Advertiser Button
| | User Click on Advertiser Created Close Button

| User Fill up the Advertiser details
| | [Documentation] | User Expected to fill up the Admin Advertiser details
| | [Arguments] | ${Test}
| | ${Data} | User Get ${test} Data
| | User Fill Up Mandetory field for Admin Advertiser | ${Data}
| | User Fill Up Primary Contact Address for Admin Advertiser | ${Data}[primary_company_address]
| | User Fill Up Secondary Contact Address 1 for Admin Advertiser | ${Data}[Secondary_company_address1]
| | User Fill Up Secondary Contact Address 2 for Admin Advertiser | ${Data}[Secondary_company_address2]

| User Get ${Test} Data
| | [Documentation] | User Expected to Fetch the test data and Return it. 
| | Log | ${pathtocsvfile}/${filename}
| | ${Data} | Get Data | ${pathtocsvfile}/${filename} | ${test}
| | [Return] | ${Data}

| User Fill Up Mandetory field for Admin Advertiser
| | [Documentation] | User Expected to Fill up the deatils for Admin advertiser Mandetory field
| | [Arguments] | ${Data}
| | User Enter Email Address | ${Data}[Email_Address] 
| | User Enter Company Site Url | ${Data}[company_site_url]
| | User Enter First Name | ${Data}[first_name]
| | User Enter Last Name | ${Data}[last_name]
| | User Enter Company Name | ${Data}[company_name]

| User Fill Up Primary Contact Address for Admin Advertiser
| | [Documentation] | User Expected to Fill up the Primary Contact Address deatils for Admin advertiser
| | [Arguments] | ${Data}
| | user enter contact name for Primary | ${Data}[primary_contact_name]
| | user enter contact email for Primary | ${Data}[primary_contact_email]
| | user enter primary address | ${Data}[address_1]
| | user enter primary address 2 | ${Data}[address_2]
| | user enter primary city | ${Data}[city]
| | user enter primary zipcode | ${Data}[zipcode]
| | user enter primary state | ${Data}[state]
| | user enter primary province | ${Data}[province]
| | user enter primary country | ${Data}[country]

| User Fill Up Secondary Contact Address 1 for Admin Advertiser
| | [Documentation] | User Expected to Fill up the Secondary Contact Address 1 deatils for Admin advertiser
| | [Arguments] | ${Data}
| | user enter contact name for secondary1 | ${Data}[primary_contact_name]
| | user enter contact email for secondary1 | ${Data}[primary_contact_email]
| | user enter secondary1 address 1 | ${Data}[address_1]
| | user enter secondary1 address 2 | ${Data}[address_2]
| | user enter secondary1 city | ${Data}[city]
| | user enter secondary1 zipcode | ${Data}[zipcode]
| | user enter secondary1 state | ${Data}[state]
| | user enter secondary1 province | ${Data}[province]
| | user enter secondary1 country | ${Data}[country]

| User Fill Up Secondary Contact Address 2 for Admin Advertiser
| | [Documentation] | User Expected to Fill up the Secondary Contact Address 2 deatils for Admin advertiser
| | [Arguments] | ${Data}
| | user enter contact name for secondary2 | ${Data}[primary_contact_name]
| | user enter contact email for secondary2 | ${Data}[primary_contact_email]
| | user enter secondary2 address 1 | ${Data}[address_1]
| | user enter secondary2 address 2 | ${Data}[address_2]
| | user enter secondary2 city | ${Data}[city]
| | user enter secondary2 zipcode | ${Data}[zipcode]
| | user enter secondary2 state | ${Data}[state]
| | user enter secondary2 province | ${Data}[province]
| | user enter secondary2 country | ${Data}[country]

| User Create a New Contract/Financial Terms
| | [Documentation] | User Expected to Create a New Admin Advertiser Contract/Financial Terms
| | [Arguments] | ${test} | ${test1} | ${Action}
| | The Application Should Be Redirected on ContractFinancialTerms
| | User Click on Create Contract Financial terms
| | User Fill up the Contract Details | ${test}
| | User Add the Contract products | ${test1} | ${Action}
| | User Click on Submit Add Advertiser Button

| User Fill up the contract details
| | [Documentation] | User Expected to Fill up the contract details
| | [Arguments] | ${test}
| | ${Data} | User Get ${test} Data
| | User Enter contract financial name | ${Data}[name]
| | User Enter contract financial terms desc | ${Data}[description]
| | User Selects the Current Date | 1
| | User Selects Contract Payment Term | ${Data}[payment_terms]
| | User Selects Contract Reporting Cycle | ${Data}[reporting_cycle]

| User Add the Contract Products
| | [Documentation] | User Expected to Add the Admin Advertiser Contract Products
| | [Arguments] | ${Test} | ${Action}
| | ${Data} | User Get ${Test} Data
| | User Add the Product | ${Action} | ${Data}
| | User Enter Pricing model
| | User Enter Adv Pricing Model amount | ${Data}
| | User Enter Adv min Spend Amount | ${Data}
| | User Enter Spend limit type
| | User Enter Number of Periods | ${Data}
| | User Enter Unit Cost Type
| | User Enter Unit Cost Amount | ${Data}

| User Add the Product
| | [Documentation] | User Expected to Add the Admin Advertiser Contract Products
| | [Arguments] | ${Action} | ${Data}
| | User Click on add Product button
| | User Enter Product name | ${Data}
| | User Enter Product category | ${Data}
| | User Enter Product brand | ${Data}
| | User Enter Product tagline | ${Data}
| | User Enter Product tags | ${Data}
| | User Selects the Country
| | User Click on assets save button

| User Save & Activate Contract
| | [Documentation] | User expected to Confirm Save & Approve the contract
| | User Confirm Save the Contract
| | User Approve the Contract

| User Craetes Product Offer Ads/Assets
| | [Documentation] | User Expected to create the Product Offer Ads/Assets 
| | [Arguments] | ${test} | ${Ad_type} | ${asset_type1} | ${asset_type2}
| | User Click on Product Offer Ads App Navig
| | User Click on Add Offer
| | ${Data} | User Get ${Test} Data
| | User Enter the add offer details | ${Data} | ${Ad_type}
| | User Click on Add Assets
| | User Add The Assets | ${asset_type1} | ${Data}
| | User Click on Add Assets
| | User Add The Assets | ${asset_type2} | ${Data}
| | User Click on Save Add Offer button
| | User validate the page and Activate the Product Offer Ads/Assets

| User Enter the add offer details
| | [Documentation] | User Expected to create the Product Offer Ads/Assets
| | [Arguments] | ${Data} | ${Ad_type}
| | User Enter Offer Name | ${Data}
| | User Selects Ad Type | ${Ad_type}
| | User Enter description | ${Data}

| User Add The Assets
| | [Documentation] | User Expected to Add Assets in the Product Offer Ads/Assets 
| | [Arguments] | ${asset_type} | ${Data}
| | User Selects Asset Type | ${asset_type}
| | IF | '${asset_type}'=='Offer Logo'
| | User Enter logo name | ${Data}[email_type_offer_logo_name]
| | User Attach doc to Assets | ${pathtocsvfile}/upload/ad5.png
| | User Click on Assets Save Button
| | ELSE IF | '${asset_type}'=='Email Offer Image'
| | User Enter logo name | ${Data}[emailOfferImage_logo_name]
| | User Enter offer click link destination url | ${Data}
| | User Enter Email offer Text | ${Data}
| | User Enter Email Subject Line text | ${Data}
| | User Enter Email Preview line text | ${Data}
| | User Enter Email ty Rewards Clicks Link Url | ${Data}
| | User Attach doc to Assets | ${pathtocsvfile}/upload/Hims_HardMints_OFFER.png
| | User Click on Assets Save Button
| | END

| User validate the page and Activate the Product Offer Ads/Assets
| | [Documentation] | User Expected Activate the Product Offer Ads/Assets
| | The Application Should Be Redirected on ProductOfferAd
| | User Activate the Product Offer

| User Creates the Campagin
| | [Documentation] | User Expected to create the Admin Advertiser Campagin 
| | [Arguments] | ${Test} | ${spend_limit_period_type}
| | User Click on Campaigns App Navig
| | The Application Should Be Redirected on Campaigns
| | User Click on Create Campaign Button
| | ${Data} | User Get ${Test} Data
| | User Enter details of edit campagin & Set Period/Budget | ${Data} |  ${spend_limit_period_type}
| | User Add product to campagin | ${Data}
| | User Click on Save Button Campaign


| User Enter details of edit campagin & Set Period/Budget
| | [Documentation] | User Expected to add/edit campagin & Set Period/Budget deatils
| | [Arguments] | ${Data} | ${spend_limit_period_type}
| | User Enter Campaign Name | ${Data}
| | User Enter Campaign Description | ${Data}
| | User click on Next Button Campaign
| | user_selects_the_campaings_current_date
| | User Selects Campaign Spend Limit Period type | ${spend_limit_period_type}
| | User Enters Campaign Spend Limit amt | ${Data} | spend_limit_amt
| | User Enter Number of Periods | ${Data}
| | User Click on Next button Campaign

| User Add Product to campagin
| | [Documentation] | User Expected to Add Product to admin advertiser campagin
| | [Arguments] | ${Data}
| | User Click on Add Product to Campaign Button
| | User Selects Product name Campaign | 0
| | User Enters Campaign spend limit amt | ${Data} | product_level_spend_limit_amt
| | User Selects Product Offer Ad Campaign
| | User Click on Save add Product to Campaign

| User Commit Campaign and Set Financials/Promotions
| | [Documentation] | User Commit the Campaign and Set Financials/Promotions
| | [Arguments] | ${Test}
| | ${Data} | User Get ${Test} Data
| | User Clicks on Campaign Edit btn
| | User Navigates to Add Product to Campagin page
| | User Save and Confirm Campaign product
| | User Clicks on Campaign Edit btn
| | User Navigates to add Product to Campagin page
| | User Set Campaign Financials and Promotions | ${Data}
| | User Click on Save Button campaign

| User Set Campaign Financials and Promotions
| | [Documentation] | User Expected to Set admin advertiser Campaign Financials and Promotions
| | [Arguments] | ${Data}
| | User Click on Set Financials Promotions btn
| | User Selects Campaign Promotion type
| | User Enters Promotion Email count | ${Data}
| | User Enters Payment amt Received | ${Data}
| | User Selects Modal Display Priority
| | User Click on Save Add Product to campaign

| User Approve and Activate the Campagin
| | [Documentation] | User Expected to Approve and Activate the Admin advertiser campagin
| | [Arguments] | ${Test} | ${Status}
| | User Click on Full Campaign view
| | User Click on Review and Approve Campaign
| | User Click on Full Campaign view
| | User Validate the Campaign Status | ${Status}
| | User Click on Campaigns App Navig
| | User Activate the Campaign