*** Settings ***

Documentation  This is basic info about suite

Library  Selenium2Library

*** Variables ***


*** Test Cases ***

User must sign in to checkout
    [Documentation]  This is basic info about test
    [Tags]  Smoke
    Open Browser  http://www.amazon.com  ff
    Maximize Browser Window
    Input Text  css=#twotabsearchtextbox  babys only
    click element  css=#nav-search > form > div.nav-right > div > input
    Sleep  3s
    Close Browser


*** Keywords ***
