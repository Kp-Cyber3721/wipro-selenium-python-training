*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    C:/Users/priya/PycharmProjects/Feb2026wiproRoboFramework/NewProject/TestData/ddtLogindata.xlsx    sheet_name=ddtLogindata
Test Template     Login Test
Suite Setup       Open Browser To Login Page
Suite Teardown    Close All Browsers

*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    chrome

*** Test Cases ***
Login With Excel Data    ${username}    ${password}

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    xpath://input[@name='username']    10s

    Input Text    xpath://input[@name='username']    ${username}
    Input Text    xpath://input[@name='password']    ${password}

    Click Button    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[contains(@class,'topbar-header')]    10s
    Element Should Be Visible        xpath://h6[contains(@class,'topbar-header')]

    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath://a[text()='Logout']    5s
    Click Element    xpath://a[text()='Logout']

    Wait Until Element Is Visible    xpath://input[@name='username']    10s