*** Settings ***
Library    SeleniumLibrary

Test Setup       Launch Browser
Test Teardown    Close Browser
Resource    ../../../RoboFrame/Resources/Resource.robot

*** Variables ***
${URL}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}     chrome
${USERNAME}    Admin
${PASSWORD}    admin123

*** Test Cases ***
TC_01 Successful Login
    Wait Until Element Is Visible    xpath://input[@name="username"]    20s
    Input Text    xpath://input[@name="username"]    ${USERNAME}
    Input Text    xpath://input[@name="password"]    ${PASSWORD}
    Click Button  xpath://button[@type="submit"]
    Wait Until Element Is Visible    xpath://h6[text()="Dashboard"]    20s

TC_02 Invalid Login
    Wait Until Element Is Visible    xpath://input[@name="username"]    20s
    Input Text    xpath://input[@name="username"]    WrongUser
    Input Text    xpath://input[@name="password"]    WrongPass
    Click Button  xpath://button[@type="submit"]
    Wait Until Element Is Visible    xpath://p[contains(@class,"alert")]    20s

TC_03 Modify Personal Details
    Wait Until Element Is Visible    xpath://input[@name="username"]    20s
    Input Text    xpath://input[@name="username"]    ${USERNAME}
    Input Text    xpath://input[@name="password"]    ${PASSWORD}
    Click Button  xpath://button[@type="submit"]

    Wait Until Element Is Visible    xpath://h6[text()="Dashboard"]    20s
    Click Element    xpath://span[text()="My Info"]

    Wait Until Element Is Visible    xpath://input[@name="firstName"]    20s
    Clear Element Text    xpath://input[@name="firstName"]
    Input Text    xpath://input[@name="firstName"]    Priyadarshee

    Wait Until Element Does Not Contain    xpath://body    oxd-form-loader    20s
    Wait Until Element Is Enabled    xpath://button[@type="submit"]    20s
    Scroll Element Into View    xpath://button[@type="submit"]

    Wait Until Keyword Succeeds    3x    2s    Click Element    xpath://button[@type="submit"]
