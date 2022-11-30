"""
File: palindrome.py
Project 7.2

"""

from arraystack import ArrayStack

def isPalindrome(string):          
    """Returns True if string is a palindrome
    or False otherwise."""
    stk = ArrayStack()
    for ch in string:
        stk.push(ch)
    for ch in string:
        if ch != stk.pop():
            return False
    return True


def main():
    while True:
        string = input("Enter a string or Return to quit: ")
        if string == "":
            break
        elif isPalindrome(string):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

main()
