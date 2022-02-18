*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  foo
    Set Password  foobar123
    Set Password Confirmation  foobar123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  f
    Set Password  foobar123
    Set Password Confirmation  foobar123
    Submit Credentials
    Register Should Fail With Message  Username minlength is 3 characters, only a-z allowed

Register With Valid Username And Too Short Password
    Set Username  foo
    Set Password  foo123
    Set Password Confirmation  foo123
    Submit Credentials
    Register Should Fail With Message  Password minlength is 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  foo
    Set Password  foo123456
    Set Password Confirmation  foobar123
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Register And Go To Login Page
    Set Username  foo
    Set Password  foobar123
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Fail Register And Go To Login Page
    Set Username  foo
    Set Password  foobar123
    Submit Login
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register And Go To Login Page
    Set Username  foo
    Set Password  foobar123
    Set Password Confirmation  foobar123
    Submit Credentials
    Go To Login Page

Fail Register And Go To Login Page
    Set Username  foo
    Set Password  foobar123
    Set Password Confirmation  foo123456
    Submit Credentials
    Go To Login Page
