import re
# Uses Support for regular expressions. 
# This module provides regular expression matching operations for strings
# re.search Scans through strings looking for a match to a parameter (returns true or false)


# Create a list to store passwords entered by the user
password_list = []


def password_strength(password):
    """
    Determines the strength of a password based on length, character variety, and common patterns.

    Input:
    password: The password to evaluate.

    Returns:
    A string indicating the password strength: "Weak", "Medium", or "Strong".
    """
    
    # The 3 strength criteria
    length_score = 0
    variety_score = 0
    pattern_score = 0

    # Scoring the password based on length. Password earns maximum points if it is longer than 10 characters
    
    if len(password) < 6:
        length_score = 1
    elif len(password) < 11:
        length_score = 2
    else:
        length_score = 3
        

    # Scoring the password based on variety:  
    
    # If the password contains both lowercase and uppercase letters, it earns a point.
    if re.search("[a-z]", password) and re.search("[A-Z]", password): 
        variety_score += 1

    # If it contains numbers, it earns a point.
    if re.search("[0-9]", password):
        variety_score += 1

    # If it contains symbols, it earns a point.
    if re.search("[!@#$%^&*()_+\-=$;':|,.<>\/?]", password):
        variety_score += 1


    # Pattern score: Deducting a point if it contains a common password
    if re.search("password", password, re.IGNORECASE) or re.search("123456789", password):
        pattern_score -= 1


    # Calculating the total score
    total_score = length_score + variety_score + pattern_score
    

    # Determining the password strength. A "strong" password has a score above 5.
    
    if total_score <= 3:
        return "Weak"
    elif total_score <= 5:
        return "Medium"
    else:
        return "Strong"


def evaluate_passwords():
    """
    Evaluates multiple passwords stored in password_list.
    Uses sequencing, selection, and iteration to provide feedback for each password.
    """
    
    # Iterate through the list of passwords and evaluate each using password_strength()
    
    for password in password_list:
        
        strength = password_strength(password) # call the procedure
        
        print("The password " + password + " is " + strength)
        

# Main program functionality

def main():
    """
    Main program to collect user passwords, evaluate them, and provide feedback.
    
    """
    while True:
        
        # Get password input from the user
        
        password = input("Enter a password or type 'done' to finish ")
        
        if password == "done":
            break
        
        password_list.append(password)


    # Call the evaluate_passwords procedure to score all passwords
    
    print("\nEvaluating your passwords:\n")
    
    evaluate_passwords()

# Start the program
main()
