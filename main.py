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
            indekss = i

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                indekss = i 
                return indekss;
            if len(opening_brackets_stack) > 0 and are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], text[i]):
                opening_brackets_stack.pop(len(opening_brackets_stack)-1)
            elif not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], text[i]):
                indekss = i
                return indekss;
    if len(opening_brackets_stack) == 0:
        indekss = 0
    return indekss;

def main():
    text = input()
    if (text[0] == "I"):
        mismatch = find_mismatch(text)
    elif (text[0] == "F"):
        f = open("steks-un-iekavas-DaviZ1986/test/", "r")
        text = f.read()
        mismatch = find_mismatch(text)
        f.close()

    if (mismatch == 0):
        print("Success")
    else:
        print(mismatch)



if __name__ == "__main__":
    main()
