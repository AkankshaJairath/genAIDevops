def password_strength(password):

    #check minimum Lenght
    if len(password) < 8:
        return False
    
    # Initilize flags for each criteria
    upper = False
    lower = False
    digit = False
    specialchar = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    #Check each character in the password

    for char in password:
        if char.isupper():
            upper = True
        elif  char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in special_characters:
            specialchar = True


    # Ensure all criteria are met
    if upper and lower and digit and specialchar:
        return True
    else:
        return False
    
def main():
         password= input("Enter the Password: ")

         if password_strength(password):
             print("Password is strong")

         else:
             print("Password is weak. It must be at least 8 characters long, contain both uppercase and lowercase letters, include at least one digit, and have at least one special character.")


if __name__ == "__main__":
      main()
