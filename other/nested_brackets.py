"""
The nested brackets problem is a problem that determines if a sequence of
brackets are properly nested.  A sequence of brackets s is considered properly nested
if any of the following conditions are true:

        - s is empty
        - s has the form (U) or [U] or {U} where U is a properly nested string
        - s has the form VW where V and W are properly nested strings

For example, the string "()()[()]" is properly nested but "[(()]" is not.

The function called is_balanced takes as input a string S which is a sequence of
brackets and returns true if S is nested and false otherwise.
"""


def is_balanced(S):

    stack = []
    open_brackets = {"(", "[", "{"}
    closed_brackets = {")", "]", "}"}
    open_to_closed = dict({"{": "}", "[": "]", "(": ")"})

    for i in range(len(S)):

        if S[i] in open_brackets:
            stack.append(S[i])

        elif S[i] in closed_brackets:
            if not stack or stack and open_to_closed[stack.pop()] != S[i]:
                return False

    return not stack


def main():
    s = input("Enter sequence of brackets: ")
    if is_balanced(s):
        print(s, "is balanced")
    else:
        print(s, "is not balanced")


if __name__ == "__main__":
    main()
