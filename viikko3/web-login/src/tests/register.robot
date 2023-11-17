*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallek
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
    Set Username  kallek
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekk
    Set Password  kalle123
    Set Password Confirmation  kalle1234
    Submit Credentials
    Registration Should Fail With Message  Password comfirmation differs from password

Login After Successful Registration
    Register Valid User
    Go To Login Page
    Set Username  testi
    Set Password  testi123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Register Invalid User
    Go To Login Page
    Set Username  t
    Set Password  testi123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Registration Should Succeed
    Main Page 2 Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Valid User
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials

Register Invalid User
    Set Username  t
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}