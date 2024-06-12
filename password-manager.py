masterpwd = input("What is the master password? ")

def view():
    print("Andrew")

def add():
    print("Andrew")

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