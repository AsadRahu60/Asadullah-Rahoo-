*** Settings ***
Documentation     UI tests against OpenCart demo.
Library           SeleniumLibrary
Resource          ../resources/ui_keywords.resource
Resource          ../resources/variables.resource
Suite Setup       Open Demo Shop Headless
Suite Teardown    Close Browser If Open
Test Teardown     Capture Page Screenshot
Test Tags         ui

*** Test Cases ***
Search Shows Results
    [Tags]    smoke
    Search For Product    ${SEARCH_TERM}
    Page Should Contain Element    css:div.product-layout

Add Product To Cart Shows Success
    Search For Product    ${SEARCH_TERM}
    Add First Result To Cart
    Page Should Contain    Success: You have added
