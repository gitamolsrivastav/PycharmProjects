*** Settings ***

Documentation  This is basic info about suite

Library  Selenium2Library









*** Variables ***


*** Test Cases ***

User must sign in to checkout
    [Documentation]  This is basic info about test
    [Tags]  Smoke
    Open Browser  http://www.amazon.com  chrome
    Close Browser


*** Keywords ***
