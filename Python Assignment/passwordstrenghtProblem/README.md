Problem Statement:
 In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the password strength. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password. 

Explanation:
Function check_password_strength(password):

  Checks if the password meets the specified criteria without using regular expressions.
  Checks for minimum length, presence of uppercase and lowercase letters, at least one digit, and at least one special character.
  
 Main function main():

Prompts the user to input a password.
Calls check_password_strength with the provided password.
Provides appropriate feedback based on whether the password meets the criteria or not.

Character Checks:

upper and lower are boolean flags to track the presence of uppercase and lowercase letters in the password.
digit checks if the password contains at least one digit using a generator expression.
pecial checks if the password contains at least one special character from the predefined special_characters string.
