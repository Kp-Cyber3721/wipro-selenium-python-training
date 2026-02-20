
*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
Library     Collections
*** Variables ***
${url}      https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Sleep    3s

    Wait Until Element Is Visible    xpath://input[@id='file-upload']

    Choose File    xpath://input[@id='file-upload']   D:/Downloads/Pytest_MCQs.docx

    Click Element    xpath://input[@id='file-submit']
    Sleep    2s
    Element Text Should Be     xpath://h3[normalize-space()='File Uploaded!']      File Uploaded!

    Sleep    2s


    Close Browser







