from cryptography.fernet import Fernet

# function to use 'cryptography' module to create a private key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def add():
    account_name = input("Account Name: ")
    account_pwd = input("Password: ")

    # Use "with" keyword to automatically close file after we are done with actions
    # "w" = write/create/override new file; "r" = read file; "a" = append mode to add at end of existing file or create new file if non-existant
    with open("vault.txt", "a") as f:
        f.write(account_name + "|" + fer.encrypt(account_pwd.encode()).decode() + "\n")

def view():
    with open("vault.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            # "rstrip" will remove the \n from the add() function when we attempt to read the file
            
            username, pwd = data.split("|")
            # "split" identifies the "|" as a separator character and then places the values before/after the separator into a list
            
            print(f"Username: {username} | Password: {fer.decrypt(pwd.encode()).decode()}")

master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

while True:
    mode = input("Add a new password or view existing ones (add, view)? Or type Q to quit: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input")
        continue

print("Exiting...")