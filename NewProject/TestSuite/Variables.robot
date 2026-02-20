*** Settings ***
Library     SeleniumLibrary
Library    OperatingSystem

*** Variables ***





${name}     John
${city}     Hyderabad
${address}      St Peter Road
@{list1}        green       red     blue
@{list2}        apple       banana      grapes
&{creds}        username=admin      password=admin123

*** Test Cases ***
verify the variables
        Log     ${name}
        Log     ${city}
        Log     ${address}
        FOR    ${element}    IN    @{list1}
            Log    ${element}

        END

        FOR    ${element}    IN    @{list2}
            Log    ${element}

        END
        Log     ${list1}[0]
        Log     ${list1}[1]
        Log     ${creds}[username]
        Log     ${creds}[password]


