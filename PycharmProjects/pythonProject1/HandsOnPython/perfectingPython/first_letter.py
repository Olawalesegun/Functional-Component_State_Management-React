def tellmeyourpasswd():
    passwordintake = input("Tell me your password\n")
    first_letter_out = passwordintake[0].upper()
    print("The first letter you entered was: " + first_letter_out)
    
tellmeyourpasswd()
