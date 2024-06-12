# python-password-manager

## Description
Organize and store passwords as encrypted credentials

## Program Logic
- Ask user for a master password to authorize access to the "vault"
    - This will be used alongside our private key to encrypt/decrypt passwords
- Ask user if they want to add a new password or view existing passwords
    - Define these selections as functions
- If adding a password, create/open a file "vault" to store the new password
    - Use `cryptography` module to encrypt password 
- If viewing passwords, output a list of passwords in existing vault
    - Use `cryptography` module to decrypt the encrypted password

## Learnings
- Functions
    - Executable and reusuable block of code
    - `def <functionname>():` to define a function
    - `<functionname>()` to call a function
- Other learnings written as comments in the code