masterpwd = input("What is the master password? ")

mode = input("Add a new password or view existing ones (add, view)? Or type Q to quit: ").lower()

while True:
    if mode == "q":
        break
    elif mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid input")
        continue

print("Exiting...")