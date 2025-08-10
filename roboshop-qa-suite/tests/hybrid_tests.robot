*** Settings ***
Documentation     Demonstration hybrid: call API, then do a UI action (conceptual linkage).
Library           SeleniumLibrary
Resource          ../resources/ui_keywords.resource
Resource          ../resources/api_keywords.resource
Resource          ../resources/variables.resource
Suite Setup       Open Demo Shop Headless
Suite Teardown    Close Browser If Open
Test Teardown     Capture Page Screenshot
Test Tags         hybrid

*** Test Cases ***
API Then UI Search (Concept Demo)
    ${resp}=    Get All Products
    ${json}=    Evaluate    ${resp.json()}
    Log    First product from API: ${json[0]['title']}
    # Use a generic term on UI since APIs and UI are separate systems
    Search For Product    ${SEARCH_TERM}
    Page Should Contain Element    css:div.product-layout
