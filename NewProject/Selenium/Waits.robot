
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
    #implicit wait - applied to all the elements
    Set Selenium Implicit Wait    2s
    #wait till the element is loaded
    Sleep    3s
    #explixit wait - wait for a particular element to be loaded
    Wait Until Element Is Visible    xpath://input[@id='file-upload']
    Set Browser Implicit Wait    2s

    Choose File    xpath://input[@id='file-upload']   C:/Users/priya/OneDrive/Desktop/Robo5.png

    Click Element    xpath://input[@id='file-submit']
    Sleep    2s
    Element Text Should Be     xpath://h3[normalize-space()='File Uploaded!']      File Uploaded!
    Sleep    2s


    Close Browser







