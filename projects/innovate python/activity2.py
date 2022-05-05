import string
import os

alphabet = string.ascii_letters

for letter in alphabet:
    print(letter)

def alphabet_index():
    res = input("Please type a number between 1 and 26: ")
    try:
        res_int = int(res)
    except:
        print("please type a number.")
        os.system('cls')
        return alphabet_index()
    print(f"The letter at index {res_int} in the alphabet is \"{alphabet[res_int - 1]}\"")
    run_again = input("Do you want to enter another number? ")
    if run_again.lower() == "n" or "no":
        return ""
    elif run_again.lower() == "y" or "yes":
        return alphabet_index()
    else:
        print("Sorry, I didn't understand that.")
        return alphabet_index()

alphabet_index() 

