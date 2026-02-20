*** Settings ***
#Testuite - set of testcases
#setting we add the external library details resources , set up and tear down commands
Library     SeleniumLibrary
#Log to console - will display on console
*** Test Cases ***
#name of the test case
verify login with valid credentials
        Log To Console     Enter Username
        Log To Console    Enter Password
        Log To Console     Click on login button
        Log To Console     user in on the home page