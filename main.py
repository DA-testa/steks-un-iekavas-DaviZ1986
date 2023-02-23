# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1 

            if not are_matching(opening_brackets_stack[-1].char, text[i]):
                return i+1
            opening_brackets_stack.pop()

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0].position
          
def main():
    ievade = input()
    if ("I" in ievade):
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)
    if ("F" in ievade):
        f = open("D:/Tests.txt", "r")
        text = f.read()
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()

