# solution : 

class Solution(object):
    def isValid(self, s):
        stack = [] 
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0

# explanation : 
# The code is a function that takes in an input string and returns True if the input is valid, otherwise it returns False.
#The code starts by creating a list of all possible pairs of brackets (') and parentheses (').
# Then for each bracket in the string, it checks to see if there are any other brackets or parentheses on either side of it.
# If so, then the bracket is appended to the stack which will be used later when checking for validity.
# If not, then len(stack) == 0 or bracket != pairs[stack.pop()] will return False because no more brackets exist on either side of this particular bracket.
# The code will return True if the input string is a valid Python expression.
