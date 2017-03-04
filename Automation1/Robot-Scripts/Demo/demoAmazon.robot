*** Settings ***

Library  Selenium2Library




*** Variables ***


*** Test Cases ***

User must check the web page for products

    [Documentation]  Basic testing
    [Tags]  Smoke

    Begin web test
    Search for products
    End web test



*** Keywords ***

Begin web test

    Open Browser  http://www.google.com  ff
    Log  browser opened successfully
    Go To  http://www.amazon.com
    Log  amazon page opened successfully


Search for products

    Maximize Browser Window
    Input Text  css=#twotabsearchtextbox  babys only
    Click Element  css=#nav-search > form > div.nav-right > div > input
    sleep  3s


End web test

    Close Browser






