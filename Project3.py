# Project 3 Python Program
# Section One
# Group Members: Jesse Adams, Dominic Orsi, Ben Puryear

import re


def main():
    # read input.txt
    file = open("file.txt")

    input = file.readlines()
    # this still includes newlines, so lets get rid of them
    for i in range(len(input)):
        input[i] = input[i].strip()

    for test_case in input:
        print("input:", test_case)
        print("DFA result:", DFA(test_case))
        print("regex result:", REGEX(test_case))


def DFA(input):
    # sigma (the alphabet)
    sigma = [0, 1]
    qs = "q000"
    # set the current state to the start state
    current_state = qs
    # accept states
    f = ["q100", "q101", "q110", "q111"]

    for val in input:
        # check to make sure that the value is in the alphabet
        if int(val) not in sigma:
            return "reject"

        if current_state == "q000":
            # q000, 0 -> q000, 1 -> q001
            if int(val) == 0:
                current_state = "q000"
            else:
                current_state = "q001"
        elif current_state == "q001":
            # q010, 0 -> q100, 1 -> q101
            if int(val) == 0:
                current_state = "q010"
            else:
                current_state = "q011"
        elif current_state == "q010":
            # q011, 0 -> q110, 1 -> q111
            if int(val) == 0:
                current_state = "q100"
            else:
                current_state = "q101"
        elif current_state == "q011":
            # q001, 0 -> q010, 1 -> q011
            if int(val) == 0:
                current_state = "q110"
            else:
                current_state = "q111"
        elif current_state == "q100":
            # q100, 0 -> q000, 1 -> q001
            if int(val) == 0:
                current_state = "q000"
            else:
                current_state = "q001"
        elif current_state == "q101":
            # q101, 0 -> q010, 1 -> q011
            if int(val) == 0:
                current_state = "q010"
            else:
                current_state = "q011"
        elif current_state == "q110":
            # q110, 0 -> q100, 1 -> q101
            if int(val) == 0:
                current_state = "q100"
            else:
                current_state = "q101"
        elif current_state == "q111":
            # q111, 0 -> q110, 1 -> q111
            if int(val) == 0:
                current_state = "q110"
            else:
                current_state = "q111"
        else:
            return "reject"  # this should never happen

    if current_state in f:
        return "accept"
    else:
        return "reject"


def REGEX(input):
    pattern = "(0|1)*1(0|1)(0|1)$"

    x = re.search(pattern, input)
    if x:
        return "accept"
    return "reject"


main()
