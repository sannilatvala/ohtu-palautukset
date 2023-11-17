*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command
    Input credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input credentials  k  kalle123
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input credentials  KALLE  kalle123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input New Command
    Input credentials  kalle  k123
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input credentials  kalle  kallekalle
    Output Should Contain  Invalid password
