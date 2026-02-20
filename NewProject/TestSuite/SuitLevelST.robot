#Test Setup -These run before  EACH test case.

#Test Teardown -These run after EACH test case.

#Suite Setup - These run only once Before all tests start

#Suite Teardown - These run only once After all tests finish



*** Settings ***
#Testuite - set of testcases
#setting we add the external library details resources , set up and tear down commands
Resource        ./../Resources/Resource.robot
Library     SeleniumLibrary
Suite Setup      Open DB
Suite Teardown       Log    Close DB

*** Test Cases ***
#name of the test case
verify login with valid credentials
    Login
verify Add to cart functionality
    Login

        Log     User selects the products
        Log     User adds the product to the cart
        Log     user verifies that the product with details is added to the cart



