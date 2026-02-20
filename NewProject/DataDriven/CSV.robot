*** Settings ***
Library     SeleniumLibrary
Library     DataDriver    C:/Users/priya/PycharmProjects/Feb2026wiproRoboFramework/NewProject/TestData/ddtLogindataCSV.csv    delimiter=;

Test Template    Login Test
Suite Setup      Open Browser To Login Page
Suite Teardown   Close All Browsers
*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    chrome
*** Test Cases ***
Login With CSV Data
*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    xpath://input[@name='username']    10s
    Input Text    xpath://input[@name='username']    ${username}
    Input Text    xpath://input[@name='password']    ${password}
    Click Button    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[contains(@class,'topbar-header')]    10s

    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible    xpath://a[text()='Logout']    5s
    Click Element    xpath://a[text()='Logout']

    Wait Until Element Is Visible    xpath://input[@name='username']    10s