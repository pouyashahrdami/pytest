# App Name : testsuite.py
# App Date : 7/25/2024
# Date Modified : 8/11/2024 => Add Report.html
# Description : Automated testing for input fields
# Programmer : Pouya Shahrdami

#---------------------------------------
# To install these dependencies, run the following command in your terminal:
# pip install -r requirements.txt
#---------------------------------------

# ====================================================================================
# * Imports
# ==================================================================================== 
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import sys
import logging
from selenium.common.exceptions import NoSuchElementException, WebDriverException
# ====================================================================================
# * End imports 
# ==================================================================================== 

# Colors 
GREEN_COLOR = "\033[92m"
YELLOW_COLOR= "\033[93m"
RESET_COLOR = "\033[0m"
# End Colors --------------------------


# ====================================================================================
# * Links Part
# ==================================================================================== 
URL = ""
ADD_CUSTOMER_PAGE = "/V4/manager/addcustomerpage.php"
EDIT_CUSTOMER_PAGE = "/V4/manager/EditCustomer.php"
EDIT_CUSTOMER = "/V4/manager/editCustomerPage.php"
DELETE_CUSTOMER = "/V4/manager/DeleteCustomerInput.php"
NEW_ACCOUNT = "/V4/manager/addAccount.php"
BALANCE_ENQUIRY = "/V4/manager/BalEnqInput.php"
MINI_STATMENT = "/V4/manager/MiniStatementInput.php"
EDIT_ACCOUNT = "/V4/manager/editAccount.php"
DELETE_ACCOUNT_INPUT = "/V4/manager/deleteAccountInput.php"
CUSTOMIZE_STATMENT = "/V4/manager/CustomisedStatementInput.php"
# ====================================================================================
# * End Link
# ==================================================================================== 


class TestBank(unittest.TestCase):

# ====================================================================================
# * Start Setup
# ==================================================================================== 
    @classmethod
    def setUpClass(cls):
        """
        This method is executed once for the entire class before any tests run.
        
        Purpose:
            1. Set up the WebDriver (in this case, Chrome) using ChromeDriver Manager.
            2. Navigate to the Guru99 demo banking website.
            3. Locate and interact with the login form elements (username, password, login button) to log into the site. 
            4. This logged-in state will persist for all subsequent test methods in the class.
        """
        try:
            cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            cls.driver.get("")
            user_name = cls.driver.find_element(By.NAME, "uid")
            password = cls.driver.find_element(By.NAME, "password")
            Submit = cls.driver.find_element(By.NAME, "btnLogin")
            user_name.send_keys("")
            password.send_keys("")
            Submit.click()
        except Exception as e:
            print(e)

    def setUp(self):
        """
        This method is executed before each individual test method runs.

        Purpose:
            1. Get the name of the current test being executed.
            2. Print a header indicating the start of the test case, with the test name formatted nicely.
        """
        try:
            test_name = self._testMethodName.replace("test_", "test : ")
            print("===============================================")
            print(f"{GREEN_COLOR}  Running Test Case: {test_name} \n{RESET_COLOR}")
        except Exception as e:
            self.fail(e)
        


    def tearDown(self):
        """
        This method is executed after each individual test method runs.

        Purpose:
            1. Get the name of the current test that just completed.
            2. Print a message indicating the completion of the test case.
        """
        try:
            test_name = self._testMethodName.replace("test_", "test : ")
            print(f"{YELLOW_COLOR}  Test Case: {test_name} Complete{RESET_COLOR}")
        except Exception as e:
            self.fail(e)    

    def select_test_cases(self):
        """
        This method presents a menu to the user for selecting which part of the 
        web application to test. Based on the user's choice, it returns a list 
        of specific test case names to execute.
        """
        while True:
            print(f"{YELLOW_COLOR}Welcome To Web Tester App{RESET_COLOR}")
            print(f"{GREEN_COLOR}\nWhich part do you want to test?{RESET_COLOR}")
            print("1. New Customer (NC)")
            print("2. Edit Customer (EC)")
            print("3. delete Customer (DC)")
            print("4. New Account (NA)")
            print("5. Edit Account (EA)")
            print("6. Delete Account (DA)")
            print("7. Balance Enquiry (BE)")
            print("8. Mini Statement (MS)")
            print("9. Customized Statement (CS)")
            print("10. All Of Theme")
            print("11. Exit")
            
            try:
                choice = input("Enter your choice (1-4): ")
                # Return list of test cases based on the user's choice
                if choice == '1':
                    return ["test_NC1_empty_value", "test_NC2_invalid_name_formats", "test_NC3_invalid_name_chars",
                            "test_NC4_Space_first", "test_NC5_Empty_Address", "test_NC6_First_Blank", "test_NC7_City_null",
                            "test_NC8_City_invalid_inputs", "test_NC9_Special_char", "test_NC10_city_first_blank",
                            "test_NC11_state_empty", "test_NC12_state_numeric", "test_NC13_state_special_chars",
                            "test_NC14_state_first_blank", "test_NC15_pin_numeric", "test_NC16_pin_empty",
                            "test_NC17_pin_digit_count", "test_NC18_pin_Special_char", "test_NC19_pin_First_blank",
                            "test_NC20_Pin_Blank_Space", "test_NC21_mobile_empty", "test_NC22_mobile_first_blank",
                            "test_NC23_mobile_with_spaces", "test_NC24_mobile_special_chars", "test_NC25_email_empty",
                            "test_NC26_email_invalid_format", "test_NC27_email_with_spaces", "test_NC28_password_empty"]
                elif choice == '2':
                    return ["test_EC1_Customer_Id_empty", "test_EC2_Customer_Id_leading_alpha",
                            "test_EC3_Customer_Id_special_chars", "test_EC4_Valid_Customer_Id",
                            "test_EC5_Address_Field_empty", "test_EC6_city_Field_empty", "test_EC7_city_numeric",
                            "test_NC28_password_empty", "test_EC9_state_Field_empty", "test_EC10_State_numeric",
                            "test_EC11_State_Special_char", "test_EC12_Pin_numeric", "test_EC13_Pin_empty",
                            "test_EC14_Pin_six_digits", "test_EC15_Pin_special_char", "test_EC16_mobile_number_empty",
                            "test_EC17_mobile_special_char", "test_EC18_mobile_number_empty",
                            "test_EC19_mobile_number_empty", "test_EC20_submit_edit_Customer"]
                elif choice == '3':
                    return ["test_DC1_Verify_CustomerID", "test_DC2_Numeric_CustomerID", "test_DC3_Special_Character",
                            "test_DC4_Blank_Space", "test_DC5_First_Character_Blank", "test_DC6_Incorrect_CustomerID",
                            "test_DC7_Correct_CustomerID", "test_DC8_Reset_Button"]
                    
                elif choice == '4':
                    return ["test_NA1_Verify_CustomerID", "test_NA2_Numeric_CustomerID", "test_NA3_Verify_CustomerID",
                            "test_NA4_Verify_CustomerID", "test_NA5_Verify_CustomerID", "test_NA6_Verify_Initial_Deposit",
                            "test_NA7_Verify_Initial_Deposit", "test_NA8_Verify_Initial_Deposit",
                            "test_NA9_Verify_Initial_Deposit", "test_NA10_Verify_Initial_Deposit",
                            "test_NA11_Verify_Account_Type", "test_NA12_Verify_Account_Type", "test_NA13_Reset_Button",
                            "test_NA14_Submit_Button", "test_NA15_Submit_Button", ]
                    
                elif choice == '5':
                    return ["test_EA1_verify_account", "test_EA2_verify_account", "test_EA3_verify_account",
                            "test_EA4_verify_account", "test_EA5_verify_account", "test_EA6_verify_submit_button",
                            "test_EA7_verify_submit_button","test_EA8_reset_button"]
                
                elif choice == '6': #delete account
                    return ["test_DA1_Account_Number_empty", "test_DA2_Verify_Numeric_Account_Number",
                            "test_DA3_Special_Character", "test_DA4_Blank_Space",
                            "test_DA5_First_Character_Blank",
                            "test_DA7_Submit_Button", "test_DA8_Reset_Button"]
                elif choice == '7': #BalanceEnquiry
                    return ["test_BE1_Account_Number_empty", "test_BE2_Numeric_Account_Number", "test_BE3_Special_Char",
                            "test_BE4_First_Character_Blank", "test_BE5_Account_invalid_number", "test_BE6_Account_reset_button"
                            ]
                elif choice == '8':  # Mini Statement
                    return ["test_MS1_Account_Number_empty", "test_MS2_Numeric_Account_Number",
                            "test_MS3_Special_Character", "test_MS4_Blank_Space", "test_MS5_First_Character_Blank",
                            "test_MS6_Account_invalid_number", "test_MS7_Account_reset_button"]
                elif choice == '9':  # Customized Statement
                    return ["test_CS1_Account_Number_empty", "test_CS2_Numeric_Account_Number", "test_CS3_Special_Char",
                            "test_CS4_Blank_Space", "test_CS5_First_Character_Blank", "test_CS6_From_Date_Field",
                            "test_CS7_To_Date_Field", "test_CS8_Numeric_Minimum_Transaction",
                            "test_CS9_Minimum_Transaction_Special_Character", "test_CS10_Blank_Space",
                            "test_CS11_First_Character_Blank", "test_CS12_Numeric_Transaction_Number",
                            "test_CS13_Transaction_Number_Special_Character", "test_CS14_Transaction_Number_Blank_Space",
                            "test_CS15_Transaction_Number_First_Character_Blank", "test_CS16_Reset_Button",
                            "test_CS17_Submit_Button"]
                    
                elif choice =='10': # Run all test cases
                    return self.get_test_case_names()  
                elif choice =='11': # Exit Application 
                    print("Bye 👋")
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                self.fail(e)


    def get_test_case_names(self):
        """
        This method dynamically gets the names of all test case methods within the class.

        Purpose: 
            - It's used to automatically discover and execute all tests when needed.
        """
        try:
            return [method for method in dir(self) if method.startswith("test_")]
        except Exception as e:
            self.fail(e)


    def assert_error_message(self, expected_message, element_id):
        """
        This method asserts that a specific error message appears in an element with the given ID.

        Purpose:
            - Ensures that error messages are correctly displayed to the user.
        """
        try:
            wait = WebDriverWait(self.driver, 2)
            error_element = wait.until(
                EC.visibility_of_element_located((By.ID, element_id))
            )
            self.assertEqual(expected_message, error_element.text)
        except Exception as e:
            self.fail(e)
            
            
    def Edit_customer_login(self, customer_id="23564"):
        """Edits a customer record using the provided customer ID.

        Args:
            customer_id: The ID of the customer to edit (defaults to "23564").
        """

        try:
            self.driver.get(URL + EDIT_CUSTOMER_PAGE)
            customer_field = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "cusid"))
            )
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "AccSubmit"))
            )
            customer_field.clear()
            customer_field.send_keys(customer_id)
            submit_button.click()

        except TimeoutException:
            self.fail("Error: Could not find the elements within the timeout period.")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")
# ====================================================================================
# * End Setup
# ==================================================================================== 


# ====================================================================================
# * START OF SECTION: New Chapter Initialization
# ==================================================================================== 

    def test_NC1_empty_value(self):  # Name cannot be empty
        """
        Test case for validating that the customer name field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.clear()
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Customer name must not be blank", "message")
        except Exception as e:  
            self.fail(f"Error in test_NC1_empty_value: {e}")


    def test_NC2_invalid_name_formats(self):
        """
        Test case for validating that the customer name field does not accept invalid formats.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.clear()
            name_field.send_keys("12345")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message")

            name_field.clear()
            name_field.send_keys("name123")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message")
        except Exception as e:
            self.fail(f"Error in test_NC2_invalid_name_formats: {e}")


    def test_NC3_invalid_name_chars(self):
        """
        Test case for validating that the customer name field does not accept special characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.clear()
            name_field.send_keys("name!@#")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message")

            name_field.clear()
            name_field.send_keys("!@#")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message")
        except Exception as e:
            self.fail(f"Error in test_NC3_invalid_name_chars: {e}")

    def test_NC4_Space_first(self):
        """
        Test case for validating that the customer name field does not allow spaces as the first character.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "name")
            name_field.clear()
            name_field.send_keys(" ")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("First character can not have space", "message")
        except Exception as e:
            self.fail(f"Error in test_NC4_Space_first: {e}")

    def test_NC5_Empty_Address(self):
        """
        Test case for validating that the address field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "addr")
            name_field.clear()
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Address Field must not be blank", "message3")
        except Exception as e:
            self.fail(f"Error in test_NC5_Empty_Address: {e}")

    def test_NC6_First_Blank(self):
        """
        Test case for validating that the address field does not allow spaces as the first character.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "addr")
            name_field.clear()
            name_field.send_keys(" ")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("First character can not have space", "message3")
        except Exception as e:
            self.fail(f"Error in test_NC6_First_Blank: {e}")

    #! test Will Fail Diffrent error message
    def test_NC7_City_null(self):
        """
        Test case for validating that the city field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            name_field = self.driver.find_element(By.NAME, "addr")
            name_field.clear()
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("City Field must be not blank", "message4")
        except Exception as e:
            self.fail(f"Error in test_NC7_City_null: {e}")

    def test_NC8_City_invalid_inputs(self):
        """
        Test case for validating that the city field does not accept invalid inputs such as numbers or alphanumeric characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            city_field = self.driver.find_element(By.NAME, "city")

            city_field.clear()
            invalid_city_numeric = "12345" 
            city_field.send_keys(invalid_city_numeric)
            city_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message4")


            city_field.clear()
            invalid_city_alphanumeric = "city123"  
            city_field.send_keys(invalid_city_alphanumeric)
            city_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message4")
        except Exception as e:
            self.fail(f"Error in test_NC8_City_invalid_inputs: {e}")

    def test_NC9_Special_char(self):  
        """
        Test case for validating that the city field does not accept special characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            city_field = self.driver.find_element(By.NAME, "city")  
            city_field.clear()
            invalid_city_1 = "City!@#"  # The first invalid input with special characters
            city_field.send_keys(invalid_city_1)
            city_field.send_keys(Keys.TAB)  
            self.assert_error_message("Special characters are not allowed", "message4")  # Assert expected error

            # Test Case 2: "!@#"
            city_field.clear()
            invalid_city_2 = "!@#"  # The second invalid input with only special characters
            city_field.send_keys(invalid_city_2)
            city_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message4")
        except Exception as e:
            self.fail(f"Error in test_NC9_Special_char: {e}")

    def test_NC10_city_first_blank(self):
        """
        Test case for validating that the city field does not allow spaces as the first character.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            city_field = self.driver.find_element(By.NAME, "city")
            city_field.clear()
            city_field.send_keys(" ")  # Enter blank space
            city_field.send_keys(Keys.TAB)
            self.assert_error_message("First character can not have space",
                                    "message4")  # Assuming "message4" is the ID for the error message element for city field
        except Exception as e:
            self.fail(f"Error in test_NC10_city_first_blank: {e}")

    def test_NC11_state_empty(self):
        """
        Test case for validating that the state field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            state_field = self.driver.find_element(By.NAME, "state")  # Assuming the state field has name "state"
            state_field.clear()
            state_field.send_keys(Keys.TAB)  # Move to the next field without entering a value
            self.assert_error_message("State must not be blank",
                                    "message5")  # Assuming "message5" is the ID for the error message element for state field
        except Exception as e:
            self.fail(f"Error in test_NC11_state_empty: {e}")

    def test_NC12_state_numeric(self):
        """
        Test case for validating that the state field does not accept numeric or alphanumeric inputs.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            state_field = self.driver.find_element(By.NAME, "state")
            state_field.clear()
            # Test Case 1: Numeric Input
            invalid_state_numeric = "1234"
            state_field.send_keys(invalid_state_numeric)
            state_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message5")

            # Test Case 2: Alphanumeric Input
            state_field.clear()
            invalid_state_alphanumeric = "State123"
            state_field.send_keys(invalid_state_alphanumeric)
            state_field.send_keys(Keys.TAB)
            self.assert_error_message("Numbers are not allowed", "message5")
        except Exception as e:
            self.fail(f"Error in test_NC12_state_numeric: {e}")
        

    def test_NC13_state_special_chars(self):
        """
        Test case for validating that the state field does not accept special characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            state_field = self.driver.find_element(By.NAME, "state")

            # Test Case 1: Special Characters
            state_field.clear()
            invalid_state = "State!@#"
            state_field.send_keys(invalid_state)
            state_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message5")

            # Test Case 2: Only Special Characters
            state_field.clear()
            invalid_state = "!@#"
            state_field.send_keys(invalid_state)
            state_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message5")
        except Exception as e:
            self.fail(f"Error in test_NC13_state_special_chars: {e}")

    # ! test will fail becuase error messages are not same
    def test_NC14_state_first_blank(self):
        """
        Test case for validating that the state field does not allow spaces as the first character.
        """

        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            state_field = self.driver.find_element(By.NAME, "state")
            state_field.clear()
            state_field.send_keys(" ")
            state_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message5")
        except TimeoutException as e:
            logging.error(f"Timeout waiting for element: {e}")
            raise
        except AssertionError as e:
            logging.error(f"Assertion failed: {e}")
            raise

    def test_NC15_pin_numeric(self):
        """
        Test case for validating that the PIN field does not accept numeric or alphanumeric inputs.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()

            # Test Case 2: "!@#"
            pin_field.clear()
            invalid_pin_2 = "1234pin"  # The second invalid input with only special characters
            pin_field.send_keys(invalid_pin_2)
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC15_pin_numeric: {e}")

    # ! test will fail becuase error messages are not same
    def test_NC16_pin_empty(self):
        """
        Test case for validating that the PIN field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(Keys.TAB)  
            self.assert_error_message("PIN code must not be blank", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC16_pin_empty: {e}")

    def test_NC17_pin_digit_count(self):
        """
        Test case for validating that the PIN field must have exactly 6 digits.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")

            # Test Case 1: More than 6 Digits
            pin_field.clear()
            pin_field.send_keys("12")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("PIN Code must have 6 Digits", "message6")

            # Test Case 2: Fewer than 6 Digits
            pin_field.clear()
            pin_field.send_keys("123")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("PIN Code must have 6 Digits", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC17_pin_digit_count: {e}")

    def test_NC18_pin_Special_char(self):
        """
        Test case for validating that the PIN field does not accept special characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")

            # Test Case 1:
            pin_field.clear()
            pin_field.send_keys("!@#")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message6")

            # Test Case 2: 
            pin_field.clear()
            pin_field.send_keys("123!@#")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC18_pin_Special_char: {e}")

    def test_NC19_pin_First_blank(self):
        """
        Test case for validating that the PIN field does not allow spaces as the first character.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(" ")
            pin_field.send_keys(Keys.TAB)  
            self.assert_error_message("First character can not have space", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC19_pin_First_blank: {e}")
        
    # ! test will fail becuase error messages are not same
    def test_NC20_Pin_Blank_Space(self):
        """
        Test case for validating that the PIN field does not accept blank spaces.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(" ")
            pin_field.send_keys(Keys.TAB)  
            self.assert_error_message("Characters are not allowed", "message6")
        except Exception as e:
            self.fail(f"Error in test_NC19_pin_First_blank: {e}")

    def test_NC21_mobile_empty(self):
        """
        Test case for validating that the mobile number field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")
            mobile_field.clear()
            mobile_field.send_keys(Keys.TAB)  
            self.assert_error_message("Mobile no must not be blank", "message7")
        except Exception as e:
            self.fail(f"Error in test_NC21_mobile_empty: {e}")

    def test_NC22_mobile_first_blank(self):  
        """
        Test case for validating that the mobile number field does not allow spaces as the first character.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")
            mobile_field.clear()
            mobile_field.send_keys(" ")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("First character can not have space", "message7")  
        except Exception as e:
            self.fail(f"Error in test_NC22_mobile_first_blank: {e}")

    def test_NC23_mobile_with_spaces(self):  
        """
        Test case for validating that the mobile number field does not accept spaces.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")
            mobile_field.clear()

            # Test Case 1: Spaces between digits
            invalid_mobile_1 = "123 123"
            mobile_field.send_keys(invalid_mobile_1)
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message7")  
        except Exception as e:
            self.fail(f"Error in test_NC23_mobile_with_spaces: {e}")

    def test_NC24_mobile_special_chars(self): 
        """
        Test case for validating that the mobile number field does not accept special characters.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")

            # Test Case 1: Special chars within number
            mobile_field.clear()
            invalid_mobile_1 = "886636!@12"
            mobile_field.send_keys(invalid_mobile_1)
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")  

            # Test Case 2: Only special chars
            mobile_field.clear()
            invalid_mobile_2 = "!@88662682"
            mobile_field.send_keys(invalid_mobile_2)
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")

            # Test Case 3: Special chars at the end
            mobile_field.clear()
            invalid_mobile_3 = "88663682!@"
            mobile_field.send_keys(invalid_mobile_3)
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")
        except Exception as e:
            self.fail(f"Error in test_NC24_mobile_special_chars: {e}")
    #! test Will Fail Diffrent error message
    def test_NC25_email_empty(self):  
        """
        Test case for validating that the email field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            email_field = self.driver.find_element(By.NAME, "emailid")
            email_field.clear()
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email ID must not be blank", "message9")
        except Exception as e:
            self.fail(f"Error in test_NC25_email_empty: {e}")

    def test_NC26_email_invalid_format(self):  
        """
        Test case for validating that the email field must be in the correct format.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            email_field = self.driver.find_element(By.NAME, "emailid")

            # Test Case 1:
            email_field.clear()
            invalid_email_1 = "guru99@gmail"
            email_field.send_keys(invalid_email_1)
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")  

            # Test Case 2:
            email_field.clear()
            invalid_email_2 = "guru99"
            email_field.send_keys(invalid_email_2)
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            # Test Case 3:
            email_field.clear()
            invalid_email_3 = "Guru99@"
            email_field.send_keys(invalid_email_3)
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            # Test Case 4:
            email_field.clear()
            invalid_email_4 = "guru99@gmail."
            email_field.send_keys(invalid_email_4)
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            # Test Case 5:
            email_field.clear()
            invalid_email_5 = "guru99gmail.com"
            email_field.send_keys(invalid_email_5)
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")
        except Exception as e:
            self.fail(f"Error in test_NC26_email_invalid_format: {e}")

    # ! will Fail problem From Wesite 
    def test_NC27_email_with_spaces(self):  
        """
        Test case for validating that the email field cannot contain spaces.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            email_field = self.driver.find_element(By.NAME, "emailid")
            email_field.clear()
            email_field.send_keys("admin @test.com")  
            email_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_NC28_password_empty(self):  
        """
        Test case for validating that the password field cannot be left empty.
        """
        try:
            self.driver.get(URL + ADD_CUSTOMER_PAGE)
            password = self.driver.find_element(By.NAME, "password")
            password.clear()
            password.send_keys(Keys.TAB)  
            self.assert_error_message("Password must not be blank", "message18")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
            
# ====================================================================================
# * End New Customer 
# ==================================================================================== 


# ====================================================================================
# * START Edit Customer Part
# ==================================================================================== 

    def test_EC1_Customer_Id_empty(self):
        """
        Test case for validating that the customer ID field cannot be left empty.
        """
        try:
            self.driver.get(URL + EDIT_CUSTOMER_PAGE)
            customer_field = self.driver.find_element(By.NAME, "cusid")
            customer_field.clear()
            customer_field.send_keys(Keys.TAB)  
            self.assert_error_message("Customer ID is required", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    #! Test Will fail No Error Gives For second part 
    def test_EC2_Customer_Id_leading_alpha(self):
        """
        Test case for validating that the customer ID field should not start with alphabets.
        """
        try:
            self.driver.get(URL + EDIT_CUSTOMER_PAGE)
            customer_field = self.driver.find_element(By.NAME, "cusid")

            # Test Case 1
            customer_field.clear()
            invalid_field1 = "Acc123"
            customer_field.send_keys(invalid_field1)
            customer_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message14")  

            # Test Case 2
            customer_field.clear()
            invalid_field2 = "1234Acc"
            customer_field.send_keys(invalid_field2)
            customer_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC3_Customer_Id_special_chars(self):
        """
        Test case for validating that the customer ID field should not contain special characters.
        """
        try:
            self.driver.get(URL + EDIT_CUSTOMER_PAGE)
            customer_field = self.driver.find_element(By.NAME, "cusid")
            customer_field.clear()
            customer_field.send_keys("123!@#")  # Input with special characters
            customer_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message14")  # Ensure this is the correct ID

            customer_field.clear()
            customer_field.send_keys("!@#")  # Input with special characters
            customer_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message14")  # Ensure this is the correct ID
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC4_Valid_Customer_Id(self):
        """
        Test case for validating that a valid customer ID allows access to the edit customer page.
        """
        try:
            self.driver.get(URL + EDIT_CUSTOMER_PAGE)
            customer_field = self.driver.find_element(By.NAME, "cusid")
            Submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            customer_field.clear()
            customer_field.send_keys("23564")  # Valid customer ID
            Submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.url_contains(EDIT_CUSTOMER))  # or some other indicator of success
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC5_Address_Field_empty(self):
        """
        Test case for validating that the address field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            address_field = self.driver.find_element(By.NAME, "addr")  # Assuming "addr" is the field name
            address_field.clear()
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Address Field must not be blank", "message3")  # Adjust the message and ID if needed
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC6_city_Field_empty(self):
        """
        Test case for validating that the city field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            city_field = self.driver.find_element(By.NAME, "city")  # Assuming "city" is the field name
            city_field.clear()
            city_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("City Field must not be blank", "message4")  # Adjust the message and ID if needed    
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC7_city_numeric(self):
        """
        Test case for validating that the city field should not contain numeric values.
        """
        try:
            self.Edit_customer_login()
            city_field = self.driver.find_element(By.NAME, "city")  # Assuming "city" is the field name
            city_field.clear()
            city_field.send_keys("1234")
            city_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Numbers are not allowed", "message4")  # Adjust the message and ID if needed    

            city_field.clear()
            city_field.send_keys("city123")
            city_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Numbers are not allowed", "message4")  # Adjust the message and ID if needed    
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
        
    def test_EC8_city_special_char(self):
        """
        Test case for validating that the city field should not contain special characters.
        """
        try:
            self.Edit_customer_login()
            address_field = self.driver.find_element(By.NAME, "city")  # Assuming "city" is the field name
            address_field.clear()
            address_field.send_keys("City!@#")
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Special characters are not allowed", "message4")  # Adjust the message and ID if needed
            
            address_field.clear()
            address_field.send_keys("!@#")
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Special characters are not allowed", "message4")  # Adjust the message and ID if needed
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
            
    #! test Will Fail Diffrent error message
    def test_EC9_state_Field_empty(self):
        """
        Test case for validating that the state field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            address_field = self.driver.find_element(By.NAME, "state")  # Assuming "state" is the field name
            address_field.clear()
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("State must be blank", "message5")  # Adjust the message and ID if needed
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC10_State_numeric(self):
        """
        Test case for validating that the state field should not contain numeric values.
        """
        try:
            self.Edit_customer_login()
            address_field = self.driver.find_element(By.NAME, "state")  # Assuming "state" is the field name
            address_field.clear()
            address_field.send_keys("1234")
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Numbers are not allowed", "message5")  # Adjust the message and ID if needed
            
            address_field.clear()
            address_field.send_keys("State123")
            address_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Numbers are not allowed", "message5")  # Adjust the message and ID if needed
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC11_State_Special_char(self):
        """
        Test case for validating that the state field should not contain special characters.
        """
        try:
            self.Edit_customer_login()
            state_field = self.driver.find_element(By.NAME, "state")  # Assuming "state" is the field name
            state_field.clear()
            state_field.send_keys("State!@#")
            state_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Special characters are not allowed", "message5")  # Adjust the message and ID if needed
            
            state_field.clear()
            state_field.send_keys("!@#")
            state_field.send_keys(Keys.TAB)  # Move focus away without entering data
            self.assert_error_message("Special characters are not allowed", "message5")  # Adjust the message and ID if needed
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
            
    #! test Will Fail Diffrent error message
    def test_EC12_Pin_numeric(self):
        """
        Test case for validating that the pin field should only contain numeric values.
        """
        try:
            self.Edit_customer_login()
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys("1234")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message6")
            
            pin_field.clear()
            pin_field.send_keys("1234PIN")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message6")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC13_Pin_empty(self):
        """
        Test case for validating that the pin field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("PIN Code must not be blank", "message6")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    # ! will Fail problem From Wesite Front part dosent let More than 6 digit so second part is OK !
    def test_EC14_Pin_six_digits(self):
        """
        Test case for validating that the pin field should contain exactly six digits.
        """
        try:
            self.Edit_customer_login()
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys("123")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("PIN Code must have 6 Digits", "message6")
            
            pin_field.clear()
            pin_field.send_keys("1234567")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("PIN Code must have 6 Digits", "message6")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC15_Pin_special_char(self):
        """
        Test case for validating that the pin field should not contain special characters.
        """
        try:
            self.Edit_customer_login()
            pin_field = self.driver.find_element(By.NAME, "pinno")
            pin_field.clear()
            pin_field.send_keys("!@#")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message6")
            
            pin_field.clear()
            pin_field.send_keys("123!@#")
            pin_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message6")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
            
    #! test Will Fail Diffrent error message
    def test_EC16_mobile_number_empty(self):
        """
        Test case for validating that the mobile number field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")
            mobile_field.clear()
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Telephone no must not be blank", "message7")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def test_EC17_mobile_special_char(self):
        """
        Test case for validating that the mobile number field should not contain special characters.
        """
        try:
            self.Edit_customer_login()
            mobile_field = self.driver.find_element(By.NAME, "telephoneno")
            mobile_field.clear()
            mobile_field.send_keys("886636!@12")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")
            
            mobile_field.clear()
            mobile_field.send_keys("!@88662682")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")
            
            mobile_field.clear()
            mobile_field.send_keys("88663682!@")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message7")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
        
    def test_EC18_mobile_number_empty(self):
        """
        Test case for validating that the mobile number field cannot be left empty.
        """
        try:
            self.Edit_customer_login()
            mobile_field = self.driver.find_element(By.NAME, "emailid")
            mobile_field.clear()
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID must not be blank", "message9")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    def test_EC19_mobile_number_empty(self):
        """
        Test case for validating that the email field should contain a valid email address.
        """
        try:
            self.Edit_customer_login()
            mobile_field = self.driver.find_element(By.NAME, "emailid")

            mobile_field.clear()
            mobile_field.send_keys("guru99@gmail")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            mobile_field.clear()
            mobile_field.send_keys("guru99")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            mobile_field.clear()
            mobile_field.send_keys("Guru99@")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")

            mobile_field.clear()
            mobile_field.send_keys("gurugmail.com")
            mobile_field.send_keys(Keys.TAB)
            self.assert_error_message("Email-ID is not valid", "message9")
        # Additional code or comments should be added here if necessary
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    def test_EC20_submit_edit_Customer(self):
        """
        Test case for validating that the edit customer form can be submitted.
        """
        try:
            self.Edit_customer_login()
            mobile_field = self.driver.find_element(By.NAME, "sub")
            mobile_field.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")


# ====================================================================================
# * End Edit Customer 
# ==================================================================================== 

# ====================================================================================
# * START BalanceEnquiry
# ==================================================================================== 


    def test_BE1_Account_Number_empty(self):
        """
        Test case for validating that the account number field cannot be left empty.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Account Number must not be blank", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    # ! test case Second Part will fail website dont give error to 1234
    def test_BE2_Numeric_Account_Number(self):
        """
        Test case for validating that the account number field should only contain numeric values.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("1234")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    def test_BE3_Special_Char(self):
        """
        Test case for validating that the account number field should not contain special characters.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("123!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    #! test Will Fail Diffrent error message
    def test_BE4_First_Character_Blank(self):
        """
        Test case for validating that the first character of the account number field cannot be a space.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys(" ")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    def test_BE5_Account_invalid_number(self):
        """
        Test case for validating that an invalid account number should trigger an alert with a specific error message.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            name_field = self.driver.find_element(By.NAME, "accountno")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            name_field.send_keys("123456")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Account does not exist"
            error_message.accept()
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")
        
    # todo :
    def test_BE6_Account_reset_button(self):
        """
        Test case for validating the functionality of the reset button in the account number field.
        """
        try:
            self.driver.get(URL + BALANCE_ENQUIRY)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            deposit_field.send_keys("qwer      123456")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Account does not exist"
            error_message.accept()
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


# ====================================================================================
# * End BalanceEnquiry
# ==================================================================================== 

# ====================================================================================
# * START Mini statement
# ==================================================================================== 


    def test_MS1_Account_Number_empty(self):
        """
        Test case for validating that the account number field cannot be left empty in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Account Number must not be blank", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    # ! test case will fail 
    def test_MS2_Numeric_Account_Number(self):
        """
        Test case for validating that the account number field should only contain numeric values in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("1234")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_MS3_Special_Character(self):
        """
        Test case for validating that the account number field should not contain special characters in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("123!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_MS4_Blank_Space(self):
        """
        Test case for validating that the account number field should not contain blank spaces in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("123 12")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    #! test will fail diffrent response
    def test_MS5_First_Character_Blank(self):
        """
        Test case for validating that the first character of the account number field cannot be a space in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys(" test")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
    
    def test_MS6_Account_invalid_number(self):
        """
        Test case for validating that an invalid account number should trigger an alert with a specific error message in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            name_field = self.driver.find_element(By.NAME, "accountno")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            name_field.send_keys("123456")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Account does not exist"
            error_message.accept()
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    def test_MS7_Account_reset_button(self):
        """
        Test case for validating the functionality of the reset button in the account number field in the mini statement section.
        """
        try:
            self.driver.get(URL + MINI_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            Reset_button = self.driver.find_element(By.NAME, "res")
            deposit_field.send_keys("qwer      123456")
            Reset_button.click()
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


# ====================================================================================
# * End Mini statement
# ==================================================================================== 


# ====================================================================================
# * START Customized statement
# ==================================================================================== 


    def test_CS1_Account_Number_empty(self):
        """
        Test case for validating that the account number field cannot be left empty in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Account Number must not be blank", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    # ! test case will fail  first part
    def test_CS2_Numeric_Account_Number(self):
        """
        Test case for validating that the account number field should only contain numeric values in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("1234")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
    
    def test_CS3_Special_Char(self):
        """
        Test case for validating that the account number field should not contain special characters in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("123!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
            
            deposit_field.clear()
            deposit_field.send_keys("!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    def test_CS4_Blank_Space(self):
        """
        Test case for validating that the account number field should not contain blank spaces in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys("123 12")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    #! test Will Fail Diffrent error message
    def test_CS5_First_Character_Blank(self):
        """
        Test case for validating that the first character of the account number field cannot be a space in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "accountno")
            deposit_field.clear()
            deposit_field.send_keys(" test")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message2")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_CS6_From_Date_Field(self):
        """
        Test case for validating that the from date field cannot be left empty in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "fdate")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("From Date Field must not be blank", "message26")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    #! test will Fail errors are not same 
    def test_CS7_To_Date_Field(self):
        """
        Test case for validating that the to date field cannot be left empty in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "tdate")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("From Date Field must not be blank", "message27")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
            
    #! test will fail second part should not give any Error
    def test_CS8_Numeric_Minimum_Transaction(self):
        """
        Test case for validating that the minimum transaction amount field should only contain numeric values in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "amountlowerlimit")
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
        try:
            deposit_field.clear()
            deposit_field.send_keys("1234")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
    
    def test_CS9_Minimum_Transaction_Special_Character(self):
        """
        Test case for validating that the minimum transaction amount field should not contain special characters in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "amountlowerlimit")
            deposit_field.clear()
            deposit_field.send_keys("123!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
        try:
            deposit_field.clear()
            deposit_field.send_keys("!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_CS10_Blank_Space(self):
        """
        Test case for validating that the minimum transaction amount field should not contain blank spaces in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "amountlowerlimit")
            deposit_field.clear()
            deposit_field.send_keys("123 12")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
    
    #! test case will fail response are not same 
    def test_CS11_First_Character_Blank(self):
        """
        Test case for validating that the first character of the amount lower limit field cannot be a space in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "amountlowerlimit")
            deposit_field.clear()
            deposit_field.send_keys(" test")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message12")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    #! test will fail second part should not give error 
    def test_CS12_Numeric_Transaction_Number(self):
        """
        Test case for validating that the number of transactions field should only contain numeric values in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "numtransaction")
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
        try:
            deposit_field.clear()
            deposit_field.send_keys("1234")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    #! test will fail the responses are not same 
    def test_CS13_Transaction_Number_Special_Character(self):
        """
        Test case for validating that the number of transactions field should not contain special characters in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "numtransaction")
            deposit_field.clear()
            deposit_field.send_keys("123!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Number of Transaction cannot have special character", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
        try:
            deposit_field.clear()
            deposit_field.send_keys("!@#")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Number of Transaction cannot have special character", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_CS14_Transaction_Number_Blank_Space(self):
        """
        Test case for validating that the number of transactions field should not contain blank spaces in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "numtransaction")
            deposit_field.clear()
            deposit_field.send_keys("123 12")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    
    #! test case will fail response are not same 
    def test_CS15_Transaction_Number_First_Character_Blank(self):
        """
        Test case for validating that the first character of the number of transactions field cannot be a space in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            deposit_field = self.driver.find_element(By.NAME, "numtransaction")
            deposit_field.clear()
            deposit_field.send_keys(" test")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("First character cannot have space", "message13")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    def test_CS16_Reset_Button(self):
        """
        Test case for validating that the reset button clears all fields in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            Account_no = self.driver.find_element(By.NAME, "accountno")
            fdate = self.driver.find_element(By.NAME, "fdate")
            tdate = self.driver.find_element(By.NAME, "tdate")
            amountlowerlimit = self.driver.find_element(By.NAME, "amountlowerlimit")
            numtransaction = self.driver.find_element(By.NAME, "numtransaction")
            reset_button = self.driver.find_element(By.NAME , "res")
            # inserting values : 
            Account_no.send_keys("123456")
            fdate.send_keys("08/02/2023")
            tdate.send_keys("08/02/2024")
            amountlowerlimit.send_keys("123")
            numtransaction.send_keys("123")
            reset_button.click()
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")
                
    #! test will fail -> website have problem {error 500}
    def test_CS17_Submit_Button(self):
        """
        Test case for validating that submitting the form with incomplete fields triggers an appropriate error message in the customize statement section.
        """
        try:
            self.driver.get(URL + CUSTOMIZE_STATMENT)
            Account_no = self.driver.find_element(By.NAME, "accountno")
            fdate = self.driver.find_element(By.NAME, "fdate")
            tdate = self.driver.find_element(By.NAME, "tdate")
            amountlowerlimit = self.driver.find_element(By.NAME, "amountlowerlimit")
            numtransaction = self.driver.find_element(By.NAME, "numtransaction")
            submit_button = self.driver.find_element(By.NAME , "AccSubmit")
            # inserting values : 
            Account_no.send_keys("123456")
            fdate.send_keys("08/02/2023")
            amountlowerlimit.send_keys("123")
            numtransaction.send_keys("123")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Please fill all fields"
            error_message.accept()
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

# ====================================================================================
# * START Customized statement
# ==================================================================================== 


# ====================================================================================
# * START Delete Customer page 
# ==================================================================================== 

 #! Test FAILED BECAUSE ACTUAL MESSAGE AND EXPECTED MESSAGE IS DIFFERENT
    def test_DC1_Verify_CustomerID(self):
        """
        Test case to verify that the Customer ID field cannot be left blank.

        This test navigates to the Delete Customer page, attempts to leave the Customer ID 
        field blank, and checks if the appropriate error message is displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            name_field.send_keys(Keys.TAB)
            self.assert_error_message("Customer ID can not be blank", "message14")  
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # characters are not allowed
    def test_DC2_Numeric_CustomerID(self):
        """
        Test case to ensure that non-numeric characters are not allowed in the Customer ID field.

        This test inputs a Customer ID containing both numbers and letters, and verifies 
        that the appropriate error message is displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            name_field.send_keys("1234Acc123")
            self.assert_error_message("Characters are not allowed", "message14")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # Special characters are not allowed
    def test_DC3_Special_Character(self):
        """
        Test case to ensure that special characters are not allowed in the Customer ID field.

        This test inputs a Customer ID containing special characters and verifies 
        that the appropriate error message is displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            name_field.send_keys("123!@#!@#")
            self.assert_error_message("Special characters are not allowed", "message14")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # Customer ID cannot have blank space
    def test_DC4_Blank_Space(self):
        """
        Test case to ensure that the Customer ID field cannot contain blank spaces.

        This test inputs a Customer ID with a blank space and verifies that the 
        appropriate error message is displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            name_field.send_keys("123 12", Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message14")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # First Character cannot be space
    def test_DC5_First_Character_Blank(self):
        """
        Test case to ensure that the first character of the Customer ID cannot be a space.

        This test inputs a Customer ID that starts with a space and verifies that the 
        appropriate error message is displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            name_field.send_keys(" ", Keys.TAB)
            self.assert_error_message("First character can not have space", "message14")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # Incorrect Customer ID
    def test_DC6_Incorrect_CustomerID(self):
        """
        Test case to verify behavior when an incorrect Customer ID is provided.

        This test inputs an incorrect Customer ID, submits the form, and verifies 
        that the appropriate alert messages are displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            name_field.send_keys("123456")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "Do you really want to delete this Customer?"
            alert.accept()  # Confirm the alert
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Customer does not exist!!"
            error_message.accept()
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except TimeoutException as e:
            self.fail(f"Timeout exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # Correct Customer ID
    def test_DC7_Correct_CustomerID(self):
        """
        Test case to verify behavior when a correct Customer ID is provided.

        This test inputs a valid Customer ID, submits the form, and checks 
        that the correct alert messages are displayed.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            customerID = ""  # -----------------------------------------------------------------------------------need valid customer id which we dont assign it to any account
            name_field.send_keys(customerID)
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "Do you really want to delete this Customer?"
            alert.accept()  # Confirm the alert
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Customer does not existcould not be deleted!! First delete all accounts of this customer then delete the customer"
            error_message.accept()
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except TimeoutException as e:
            self.fail(f"Timeout exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

    # check reset button if working  
    def test_DC8_Reset_Button(self):
        """
        Test case to verify the functionality of the reset button.

        This test inputs a Customer ID, clicks the reset button, and checks 
        that the Customer ID field is cleared.
        """
        try:
            self.driver.get(URL + DELETE_CUSTOMER)
            name_field = self.driver.find_element(By.NAME, "cusid")
            reset_button = self.driver.find_element(By.NAME, "res")
            name_field.send_keys("12456xoieqwsdn")
            reset_button.click()
            self.assertEqual(name_field.get_attribute('value'), '', "Customer ID field is not reset")
        except NoSuchElementException as e:
            self.fail(f"Element not found: {e}")
        except WebDriverException as e:
            self.fail(f"WebDriver exception: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")

# ====================================================================================
# * End Delete Customer page 
# ====================================================================================


# ====================================================================================
# * START New Account page 
# ====================================================================================
# Verify Customer id
    def test_NA1_Verify_CustomerID(self):
        """
        Test that verifies if the Customer ID field is required.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            customerid_field.send_keys(Keys.TAB)
            self.assert_error_message("Customer ID is required", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Customer id must be numeric
    def test_NA2_Numeric_CustomerID(self):
        """
        Test that verifies the Customer ID field only accepts numeric input.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            customerid_field.send_keys("1234Acc")
            self.assert_error_message("Characters are not allowed", "message14")
            customerid_field.clear()
            customerid_field.send_keys("Acc123")
            self.assert_error_message("Characters are not allowed", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Customer id cannot have special character
    def test_NA3_Verify_CustomerID(self):
        """
        Test that verifies the Customer ID field does not accept special characters.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            customerid_field.send_keys("123!@#")
            self.assert_error_message("Special characters are not allowed", "message14")
            customerid_field.clear()
            customerid_field.send_keys("!@#")
            self.assert_error_message("Special characters are not allowed", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Customer id cannot have blank space
    def test_NA4_Verify_CustomerID(self):
        """
        Test that verifies the Customer ID field does not accept blank spaces.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            customerid_field.send_keys("123 12", Keys.TAB)
            self.assert_error_message("Characters are not allowed", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # First Character cannot be space
    def test_NA5_Verify_CustomerID(self):
        """
        Test that verifies the Customer ID field does not allow the first character to be a space.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            customerid_field.send_keys(" ", Keys.TAB)
            self.assert_error_message("First character can not have space", "message14")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Cannot be empty
    def test_NA6_Verify_Initial_Deposit(self):
        """
        Test that verifies the Initial Deposit field is required and cannot be empty.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            deposit_field.send_keys(Keys.TAB)
            self.assert_error_message("Initial Deposit must not be blank", "message19")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Initial deposit must be numeric
    def test_NA7_Verify_Initial_Deposit(self):
        """
        Test that verifies the Initial Deposit field only accepts numeric input.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            deposit_field.send_keys("1234Acc")
            self.assert_error_message("Characters are not allowed", "message19")
            deposit_field.clear()
            deposit_field.send_keys("Acc123")
            self.assert_error_message("Characters are not allowed", "message19")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Initial deposit cannot have special character
    def test_NA8_Verify_Initial_Deposit(self):
        """
        Test that verifies the Initial Deposit field does not accept special characters.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            deposit_field.send_keys("123!@#", Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message19")
            deposit_field.clear()
            deposit_field.send_keys("!@#", Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message19")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Initial Deposit cannot have blank space
    #! failed beacuse expected result did not match************************************************************FAILED
    def test_NA9_Verify_Initial_Deposit(self):
        """
        Test that verifies the Initial Deposit field does not accept blank spaces.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            deposit_field.send_keys("123 12", Keys.TAB)
            self.assert_error_message("Special characters are not allowed", "message19")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # First Character cannot be space
    def test_NA10_Verify_Initial_Deposit(self):
        """
        Test that verifies the Initial Deposit field does not allow the first character to be a space.

        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            deposit_field.send_keys(" ", Keys.TAB)
            self.assert_error_message("First character can not have space", "message19")
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Verify Account type dropdown - select savings
    def test_NA11_Verify_Account_Type(self):
        """
        Test that verifies the Account Type dropdown can select the 'Savings' option.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            account_dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
            account_dropdown.select_by_visible_text("Savings")
            selected_option = account_dropdown.first_selected_option.text
            self.assertEqual(selected_option, 'Savings')
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Verify Account type dropdown - select current
    def test_NA12_Verify_Account_Type(self):
        """
        Test that verifies the Account Type dropdown can select the 'Current' option.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            account_dropdown = Select(self.driver.find_element(By.NAME, "selaccount"))
            account_dropdown.select_by_visible_text("Current")
            selected_option = account_dropdown.first_selected_option.text
            self.assertEqual(selected_option, 'Current')
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Reset Button
    def test_NA13_Reset_Button(self):
        """
        Test that verifies the Reset button clears all fields.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            reset_button = self.driver.find_element(By.NAME, "reset")
            deposit_field.send_keys("qwer")
            customerid_field.send_keys("123456")
            reset_button.click()
            self.assertEqual(customerid_field.get_attribute('value'), '')
            self.assertEqual(deposit_field.get_attribute('value'), '')
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Submit button - Incorrect Customer ID
    def test_NA14_Submit_Button(self):
        """
        Test that verifies the Submit button shows an alert for an incorrect Customer ID.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            submit_button = self.driver.find_element(By.NAME, "button2")
            customerid_field.send_keys("123456789")
            deposit_field.send_keys("2000")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Customer does not exist!!"
            error_message.accept()
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")


    # Submit button - Correct Customer ID and correct amount
    #! TEST FAILED - different acknowledgement text than expected---------------------------------------FAILED
    def test_NA15_Submit_Button(self):
        """
        Test that verifies the Submit button works correctly with valid input.
        """
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            submit_button = self.driver.find_element(By.NAME, "button2")
            customerid_field.send_keys("51407")
            deposit_field.send_keys("1000")
            submit_button.click()
            error_message = self.driver.find_element(By.CLASS_NAME, "heading3")
            self.assertEqual(error_message.text, 'Account generated succussfully')#!   <<<--------------------
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
    

    def test_NA16_Continue_Link(self):
        """
        Click on Continue hyperlink on next page after successful creation of account and confirm homepage with manager id
        """ 
        try:
            self.driver.get(URL + NEW_ACCOUNT)
            customerid_field = self.driver.find_element(By.NAME, "cusid")
            deposit_field = self.driver.find_element(By.NAME, "inideposit")
            submit_button = self.driver.find_element(By.NAME, "button2")
            customerid_field.send_keys("23564")
            deposit_field.send_keys("4000")
            submit_button.click()
            wait = WebDriverWait(self.driver, 10)
            continue_link = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//td[@colspan='2']/a[@href='Managerhomepage.php']"))
            )
            continue_link.click()
            # we will use manager ID to confirm the homepage
            manager_id = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//tr[@class='heading3']/td"))
            )
            self.assertEqual(manager_id.text, 'Manger Id : mngr585278')
        except Exception as e:
            self.fail(f"Test failed due to: {e}")   
        
            
# ====================================================================================
# * End New Account page 
# ====================================================================================


# ====================================================================================
# * Edit Account page
# ====================================================================================     
    
    #! Test failed because of different error message------------------------------------------------------FAILED
    def test_EA1_verify_account(self):
        """
        Account number cannot be empty
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys(Keys.TAB)
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Account Number must not be empty")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
    
    def test_EA2_verify_account(self):
        """
        Account number must be numeric
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("1234Acc123")
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Characters are not allowed")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
    
    
    def test_EA3_verify_account(self):
        """
        Account number cannot have special character
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("123!@#!@#")
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Special characters are not allowed")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
            
    def test_EA4_verify_account(self):
        """
        Account number cannot have blank space
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("123 12")
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Characters are not allowed")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
            
    
    #! test failed - different error message ----------------------------------------------------FAILED
    def test_EA5_verify_account(self):
        """
        First Character cannot be space
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys(" ",Keys.TAB)
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "First character cannot have space")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
    

    def test_EA6_verify_submit_button(self):
        """
        check with valid account no
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("136724")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            current_url = self.driver.current_url
            self.assertEqual(current_url, URL + "/V4/manager/editAccountPage.php")
        except Exception as e:
            self.fail(f"Test failed due to: {e}")
    
    def test_EA7_verify_submit_button(self):
        """
        InValid Account Number
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("12345")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            error_message = self.driver.switch_to.alert
            assert error_message.text == "Account does not exist"
            error_message.accept()
        except Exception as e:
            self.fail(f"Test failed due to: {e}")  
    

    def test_EA8_reset_button(self):
        """
        verify if reset button is working properly
        """
        try:
            self.driver.get(URL + EDIT_ACCOUNT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("qwer1354")
            reset_button = self.driver.find_element(By.NAME, "res")
            reset_button.click()
            self.assertEqual(account_field.get_attribute("value"), "")
        except Exception as e:
            self.fail(f"Test failed due to: {e}") 
            
# ====================================================================================
# * End Edit Account page
# ====================================================================================       


# ====================================================================================
# * Delete Account Page starts here
# ====================================================================================       

    def test_DA1_Account_Number_empty(self):
        """
        Account number cannot be empty
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys(Keys.TAB)
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Account Number must not be blank")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    def test_DA2_Verify_Numeric_Account_Number(self):
        """
        Account number must be numeric
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("1234Acc123")
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Characters are not allowed")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    def test_DA3_Special_Character(self):
        """
        Account number cannot have special character
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("123!@#!@#")
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Special characters are not allowed")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    def test_DA4_Blank_Space(self):
        """
        Account number cannot have blank space
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("123 12", Keys.TAB)
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "Characters are not allowed")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    #! Test Failed - Different error message-----------------------------------------------------FAILED
    def test_DA5_First_Character_Blank(self):
        """
        First Character cannot be space
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys(" ", Keys.TAB)
            error_message = self.driver.find_element(By.ID, "message2")
            self.assertEqual(error_message.text, "First character cannot have space")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    #! TEST FAILED - Website have Problem -------------------------------------------FAILED
    # def test_DA6_Submit_Button(self):
    #     """
    #     enter valid Account Number
    #     """
    #     try:
    #         self.driver.get(URL + DELETE_ACCOUNT_INPUT)
    #         account_field = self.driver.find_element(By.NAME, "accountno")
    #         account_field.send_keys("136723")
    #         submit_button = self.driver.find_element(By.NAME, "AccSubmit")
    #         submit_button.click()
    #         WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    #         alert = self.driver.switch_to.alert
    #         assert alert.text == "Do you really want to delete this Account?"
    #         alert.accept()  # Press ok
    #         WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    #         confirmation = self.driver.switch_to.alert
    #         assert confirmation.text == "Account deleted successfully"
    #         confirmation.accept()
    #     except Exception as e:
    #         self.fail(f"Test falied due to: {e}")
    
    def test_DA7_Submit_Button(self):
        """
        Enter invalid Account Number
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("12345")
            submit_button = self.driver.find_element(By.NAME, "AccSubmit")
            submit_button.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == "Do you really want to delete this Account?"
            alert.accept()  # Press ok
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            confirmation = self.driver.switch_to.alert
            assert confirmation.text == "Account does not exist"
            confirmation.accept()
        except Exception as e:
            self.fail(f"Test falied due to: {e}")
    
    def test_DA8_Reset_Button(self):
        """
        verify reset button if its working properly
        """
        try:
            self.driver.get(URL + DELETE_ACCOUNT_INPUT)
            account_field = self.driver.find_element(By.NAME, "accountno")
            account_field.send_keys("qwer123")
            reset_button = self.driver.find_element(By.NAME, "res")
            reset_button.click()
            self.assertEqual(account_field.get_attribute("value"), "")
        except Exception as e:
            self.fail(f"Test falied due to: {e}")


# ====================================================================================
# * Delete Account Page ends here
# ====================================================================================       


# ====================================================================================
# * Run App part 
# ====================================================================================

    @classmethod
    def tearDownClass(cls):
        try:
            cls.driver.quit()
        except Exception as e:
            print(f"Test falied due to: {e}")


if __name__ == "__main__":
    try:
        test_bank = TestBank()
        test_cases_to_run = test_bank.select_test_cases()
        if test_cases_to_run:
            suite = unittest.TestSuite()
            for test_name in test_cases_to_run:
                suite.addTest(TestBank(test_name))
            unittest.TextTestRunner().run(suite)
        test_bank.tearDownClass() 
    except Exception as e:
        print(f"Test falied due to: {e}")
# ====================================================================================
# * End App part 
# ====================================================================================