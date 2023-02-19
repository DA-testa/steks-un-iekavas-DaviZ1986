# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(text[i])
            indekss = i+1

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                indekss = i+1 
                return indekss;
            if len(opening_brackets_stack) > 0 and are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], text[i]):
                opening_brackets_stack.pop(len(opening_brackets_stack)-1)
            elif not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], text[i]):
                indekss = i + 1
                return indekss;
    if len(opening_brackets_stack) == 0:
        indekss = 0
    return indekss;

def main():
    text = input()
    mismatch = find_mismatch(text)
    if (mismatch == 0):
        print("Success")
    else:
        print(mismatch)



if __name__ == "__main__":
    main()
