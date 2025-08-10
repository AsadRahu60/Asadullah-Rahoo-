*** Settings ***
Library    SeleniumLibrary
Resource   variables.resource

*** Keywords ***
Open Demo Shop
    Open Browser    ${UI_BASE}    ${BROWSER}
    Maximize Browser Window

Open Demo Shop Headless
    Open Browser    ${UI_BASE}    ${HEADLESS}

Search For Product
    [Arguments]    ${term}
    Input Text    css:input[name='search']    ${term}
    Click Button  css:button.btn.btn-default.btn-lg
    Wait Until Page Contains Element    css:div.product-layout    10s

Add First Result To Cart
    Click Button    xpath=(//button[@data-original-title='Add to Cart'])[1]
    Wait Until Page Contains    Success: You have added    10s

Go To Cart Page
    Click Element   css:#top-links a[title='Shopping Cart']

Close Browser If Open
    Run Keyword And Ignore Error    Close All Browsers
