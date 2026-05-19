"""
Task description
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.
"""

# My Solution

def solution(S):
    # Implement your solution here
    right = len(S) - 1
    left = 0
    while left < right:
        if (S[left] == '(' and S[right] != ')') or (S[left] == '[' and S[right] != ']') or (S[left] == '{' and S[right] != '}'):
            return 0
        right -= 1
        left += 1

    return 1

    pass

# My new solution

def solution(S):
    # Implement your solution here
    string = []
    for i in S:
        if i == '(' or i == '{' or i == '[':
            string.append(i)
        else:
            if len(string) == 0:
                return 0

            comp = string.pop()
            if i == '}' and comp != '{':
                return 0
            elif i == ')' and comp != '(':
                return 0
            elif i == ']' and comp != '[':
                return 0
    
    if len(string) == 0:
        return 1
    else: 
        return 0 

    pass

# Optimized Solution

def solution(S):
    stack = []
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in S:
        # If it's an opening bracket, push it to the stack
        if char in bracket_map.values():
            stack.append(char)
            
        # If it's a closing bracket
        elif char in bracket_map.keys():
            # 1. Check if stack is empty (too many closing brackets)
            if len(stack) == 0:
                return 0
                
            # 2. Pop the last opening bracket and compare
            comp = stack.pop()
            if comp != bracket_map[char]:
                return 0
                
    # At the end, the stack should be empty. 
    # If it's not, there were unmatched opening brackets.
    if len(stack) == 0:
        return 1
    else:
        return 0