*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  foo  foobar123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  ada123456
    Output Should Contain  Username minlength is 3 characters, only a-z allowed

Register With Valid Username And Too Short Password
    Input Credentials  foo  123
    Output Should Contain  Password minlength is 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  foo  foobardoe
    Output Should Contain  Password has to contain at least 1 non-letter

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
