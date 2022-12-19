# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Note: to check if a string is a palindrome is basically if it reads the same way as it does when it is reversed

# Type : O(n)

class Solution(object):
    def isPalindrome(self, s):
        # Building a newStr variable that is removing all non-alphanumerical charactersm from the input string
        newStr = ""
        # we are going to iterate through every character in the sting s
        for char in s:
            # Checking to see if a character is alphanumerical with the built in function .isalnum()
            if char.isalnum():
                # If the char is alphanumerical we want to include it in the new string 
                # we also want to make sure every char is lowercase
                newStr += char.lower()
        # Checking if the new string is the exact same when reversed
        # If equal it will return true, in not equal it will return false 
        return newStr == newStr [::-1]



# Two pointer system to see whether this is a palindrome or not

class Solution(object):
    def isPalindrome(self, s):
        # Intailizing leftpt to 0 and rightpt to length of the string minus 1
        leftpt, rightpt = 0, len(s) - 1
        # Checking if it is  a palindrome while the leftpt is less than the rightpt
        while leftpt < rightpt:
            # Run these while loops to make sure that the char is alphanumeric
            while leftpt < rightpt and not self.alphaNum(s[leftpt]):
                leftpt += 1
            while rightpt > leftpt and not self.alphaNum(s[rightpt]):
                rightpt -= 1
            # If the char at the leftpt and rightpt is not equal return false
            if s[leftpt].lower() != s[rightpt].lower():
                return False
            # Use this to continue to compare the next position of the string
            leftpt, rightpt = leftpt + 1, rightpt - 1
        return True




    def alphaNum(self, char):
        # Using ord will return ascii value of characters
        # Use this to check if there is a uppercase value, ascii values are contiguous for uppercase characters
        # So if the ascii value of char is between A and Z, that means its an uppercase character
        # So if the ascii value of char is between a and z, that means its an lowercase character
        # If any of the three statments are true this will be true
        # If its alphanumeric it will return true if it not alphanumeric it will return false
        # This is just the helper function
        return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))