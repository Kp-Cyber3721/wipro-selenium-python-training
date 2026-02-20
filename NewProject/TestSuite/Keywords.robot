*** Settings ***
#Testuite - set of testcases
#setting we add the external library details resources , set up and tear down commands
Library     SeleniumLibrary
*** Test Cases ***
#name of the test case
verify login with valid credentials
            Login

verify Add to cart functionality
            Login
        Log     User selects the products
        Log     User adds the product to the cart
        Log     user verifies that the product with details is added to the cart

*** Keywords ***
Login
        Log     Enter Username
        Log     Enter Password
        Log     Click on login button
        Log     user in on the home page

