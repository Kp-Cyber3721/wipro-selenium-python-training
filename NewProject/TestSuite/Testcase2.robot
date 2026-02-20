*** Settings ***
#Testuite - set of testcases
#setting we add the external library details resources , set up and tear down commands
Library     SeleniumLibrary
#Log - will display in the report
*** Test Cases ***
#name of the test case
verify login with valid credentials
        Log     Enter Username
        Log     Enter Password
        Log     Click on login button
        Log     user in on the home page