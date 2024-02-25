# Write your application keywords
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json
from utils.generic_keywords import *
import datetime
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from datetime import timedelta
from openapi_schema_validator import validate
from modules import *


def Scroll_to_element(locator, value=100):
    """
    This function scrolls the webpage to a specified element using SeleniumLibrary in Python.
    :param locator: The locator is a string that represents the way to locate the element on the
    webpage.
    :param value: The value parameter is an optional parameter that specifies the amount of pixels to
    scroll up or down from the element's location.
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    xy_value = ele.location
    se2lib.driver.execute_script("window.scrollTo(0, " + str(xy_value['y']-value)+");")
    time.sleep(4)


def mouse_over_to_element(locator):
    """
    This function moves the mouse over to a specified element using Selenium's ActionChains.
    :param locator: The locator parameter is a string that represents the XPath of the element that the
    mouse should be moved over to
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, locator)
    action = ActionChains(se2lib.driver)
    action.move_to_element(ele).perform()
    time.sleep(3)


def path_to_json_file(path_to_json_file, filename):
    """
    This function takes a path to a JSON file and a filename and returns the full path to the JSON file.
    :param path_to_json_file: A string representing the path to the directory where the JSON file is
    located
    :param filename: The name of the JSON file without the ".json" extension
    :return: a string that concatenates the `path_to_json_file`, `filename`, and the file extension
    `.json`. This string represents the full path to a JSON file.
    """
    return (path_to_json_file + filename + ".json")


def check_testRunStatus_enabled(filename):
    """This function reads a JSON file and returns a list of tests that have the "testRunEnabled" attribute
    set to "True".
    :param filename: The name or path of the JSON file that contains the test data
    :return: a list of dictionaries containing information about the tests that have the
    "testRunEnabled" key set to the string value "True" in a JSON file specified by the "filename"
    parameter.
    """
    path = filename
    json_file = open(path, 'r')
    data = json.load(json_file)
    test_list = []
    test_num = [i for i, d in enumerate(data['testList']) if d['testRunEnabled'] == 'True']
    # print(test_num)
    for test_index in test_num:
        if test_num is None:
            print("no of tests are selected for execution : ", str(0))
        else:
            test_list.append(data['testList'][test_index])
            Tests = data["testList"][test_index]
            print(Tests['test_name'])
    json_file.close()
    return test_list


def Get_Seconds_From_Time(input_time):
    """
    The function takes a time in the format of minutes and seconds separated by a colon and returns the
    total number of seconds.
    :param input_time: A string representing time in the format "mm:ss" where mm represents minutes and
    ss represents seconds
    :return: the total number of seconds in the input time, which is calculated by converting the
    minutes to seconds and adding them to the seconds value.
    """
    min, sec = input_time.split(':')
    return int(min) * 60 + int(sec)


def does_element_exist(element):
    """This function checks if an element exists on a webpage and returns a boolean value.
    :param element: The element is a string parameter that represents the identifier of the web element
    that needs to be checked for existence
    :return: a boolean value - True if the element exists and False if it does not exist.
    """
    log_method("custom_keywords", "does element exists: " + element)
    try:
        return verify_element_on_load(element)

    except Exception as e:
        log_method("custom_keywords", "element does not exists: " + element)
        return False


def log_method(file_name, message):
    """The function takes in a file name and a message and prints them in a specific format.
    :param file_name: The name of the Python file where the log message is being generated
    :param message: It is a string that represents the log message that we want to print
    """
    print(f"{file_name}.py | {message}")


def element_by_javascript(xpath):
    """
    Click button by javascript using xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    # se2lib.driver.execute_script("arguments[0].scrollIntoView();", ele)
    wait = WebDriverWait(se2lib.driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.click()
    # se2lib.driver.execute_script("arguments[0].click();", ele)


def input_by_javascript(xpath, text):
    """
    Enter Text into text box by javascript using xpath
    :param xpath
    """
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    ele = se2lib.driver.find_element(By.XPATH, xpath)
    se2lib.driver.execute_script(f"arguments[0].sendKeys({text});", ele)


def capture_date_time(time):
    """This function captures a date and time from a given input and returns it in a specific format.
    :param time: The input parameter "time" is a string that represents a timestamp in milliseconds
    :return: a formatted date string in the format of "Month, Day Year" if the input time is in a valid
    format, otherwise it returns the string "Invalid time format".
    """
    time_digits = re.sub('[^0-9]', '', time)
    if time_digits:
        return datetime.datetime.fromtimestamp(int(time_digits) / 1000).strftime('%B, %d %Y')
    else:
        return "Invalid time format"


def day_to_time_conversion(time_input):
    """
     This function converts day to time format
    """
    if "d ago" in time_input:
        n = time_input.replace("d ago", "").replace("()", "")
        current_date = datetime.datetime.now()
        days_back = current_date - timedelta(days=int(n))
        formatted_date = days_back.strftime("%B, %d %Y")
        return formatted_date
    return time_input

def return_response_data(data):
    """ the function Returns values in the form of dict for validating request response payload
    """
    return dict(data)

def validate_the_data_with_schema(schema, data):
    """The function "validate_the_data_with_schema" validates the given data against a given schema.

    :param schema: The schema parameter is a JSON schema that defines the structure and validation rules
    for the data. It specifies the expected data types, formats, and constraints for each field in the
    data
    :param data: The data parameter is the data that you want to validate against the schema. It can be
    any type of data, such as a dictionary, list, or string
    """
    validate(schema, data)

def concatenate_the_two_string_with(string_1, string_2):
    """The function concatenates two strings and converts the result into a float.

    :param string_1: The parameter `string_1` is the first string that you want to concatenate
    :param string_2: The parameter `string_2` is a string that will be concatenated with `string_1` to
    form a new string
    :return: a float value.
    """
    data = {"Authorization": f"{string_1}{string_2}"}
    print (data)
    return (dict(data))

def get_data(filename, attribute):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data[0][attribute]['data']