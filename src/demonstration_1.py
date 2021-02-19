"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    result = ""

    for char in string:
        num = ord(char)

        # Add 32 to num if it falls within this range
        if num >= 65 and num <= 90:
            num += 32

        result += chr(num)

    return result

print(to_lower_case("LoL"))
print(to_lower_case("Hello World"))
print(to_lower_case("Test Test !@#"))

