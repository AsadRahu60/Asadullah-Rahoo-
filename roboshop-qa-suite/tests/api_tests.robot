*** Settings ***
Documentation     API tests against Fake Store API.
Resource          ../resources/api_keywords.resource
Resource          ../resources/variables.resource
Suite Setup       Create API Session
Test Tags         api

*** Test Cases ***
Get Products Returns 200 And List
    ${resp}=    Get All Products
    ${json}=    Evaluate    ${resp.json()} 
    Should Be True    len(${json}) > 0
    Dictionary Should Contain Key    ${json[0]}    title

Create Product Returns Success
    ${resp}=    Create Product    Robot Widget    29.99    gadgets
    ${json}=    Evaluate    ${resp.json()}
    Dictionary Should Contain Key    ${json}    id
    Should Be Equal    ${json['title']}    Robot Widget
