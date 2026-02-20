*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}        https://the-internet.herokuapp.com/download
${FILE}       upload.txt
${DOWNLOADS}  D:/Downloads

*** Test Cases ***
Download File
    Open Browser    ${URL}    chrome
    Click Link    ${FILE}

    Wait Until Keyword Succeeds    10x    1s
    ...    File Should Exist    ${DOWNLOADS}/${FILE}

    Close Browser
