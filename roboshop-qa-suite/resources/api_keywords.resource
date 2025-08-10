*** Settings ***
Library    RequestsLibrary
Resource   variables.resource

*** Keywords ***
Create API Session
    Create Session    fakestore    ${API_BASE}

Get All Products
    ${resp}=    GET On Session    fakestore    /products
    Should Be Equal As Integers    ${resp.status_code}    200
    [Return]    ${resp}

Create Product
    [Arguments]    ${title}=Robot Widget    ${price}=19.99    ${category}=electronics
    ${payload}=    Create Dictionary    title=${title}    price=${price}    category=${category}
    ${resp}=    POST On Session    fakestore    /products    json=${payload}
    Should Be True    ${resp.status_code} == 200 or ${resp.status_code} == 201
    [Return]    ${resp}
