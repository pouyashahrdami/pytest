# Guru99 Bank Test Suite

  

This test suite is designed to automate the testing of various functionalities within the Guru99 demo banking website. The suite is built using Selenium WebDriver and unittest framework.

* * *

  

# Features

**Comprehensive Coverage**: Tests different sections of the web application, including New Customer, Edit Customer, Delete Customer, New Account, Edit Account, Delete Account, Balance Enquiry, Mini Statement, and Customized Statement.

**Robust Validation**: Includes test cases for verifying proper input handling (e.g., empty fields, invalid formats, special characters), as well as testing the success and error scenarios for various operations.

**User-Friendly**: Offers an interactive menu to select specific test cases or run all of them.

**Clear Reporting**: Provides detailed test case names and results, with color-coded formatting for better readability.

Setup

  

* * *

# Prerequisites:

  

- Python (3.x recommended)
- Selenium WebDriver
- WebDriver Manager
- unittest
- Installation:

  

Install required packages: `pip install selenium webdriver-manager`

# 

* * *

## Execution:

- Run the script from your terminal: `python your_script_name.py`
- The interactive menu will prompt you to choose which test cases to execute.

  

* * *

## Code Structure

- Imports: Includes necessary modules from selenium, unittest, webdriver\_manager, and sys.
- Links: Defines URLs for different pages within the banking website.
- Colors: Defines ANSI escape codes for color-coded output.
- TestBank Class:
    - setUpClass: Sets up the WebDriver, navigates to the website, and logs in.
    - setUp: Prints a header for each test case.
    - tearDown: Prints a completion message for each test case.
    - select\_test\_cases: Displays the interactive menu and returns the selected test case names.
- Test Case Methods: Individual test methods for different functionalities, named according to the section and specific scenario they test (e.g., test\_NC1\_empty\_value, test\_EC2\_Customer\_Id\_leading\_alpha).