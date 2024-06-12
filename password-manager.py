master_pwd = input("What is the master password? ")

def view():
    print("Andrew")

def add():
    account_name = input("Account Name: ")
    account_pwd = input("Password: ")

    # Use "with" keyword to automatically close file after we are done with actions
    # "w" = write/create/override new file; "r" = read file; "a" = append mode to add at end of existing file or create new file if non-existant
    with open("vault.txt", "a") as f:

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