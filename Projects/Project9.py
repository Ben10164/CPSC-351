"""
Jesse Adams, Domonic Orsi, Ben Puryear
12/11/2023
CPSC 351-01 (Section 1)
Project 9 (Q4)
"""


def run(input_string):
    # this delta dictionary will be set up as follows:
    #   (current state, read symbol): (destination state, write symbol, move direction)
    delta = {
        # q1
        ("q1", "U"): ("qreject", "U", "R"),
        ("q1", "X"): ("qreject", "X", "R"),
        ("q1", "0"): ("q2", "U", "R"),
        # q2
        ("q2", "U"): ("qaccept", "U", "R"),
        ("q2", "X"): ("q2", "X", "R"),
        ("q2", "0"): ("q3", "X", "R"),
        # q3
        ("q3", "U"): ("q5", "U", "L"),
        ("q3", "X"): ("q3", "X", "R"),
        ("q3", "0"): ("q4", "0", "R"),
        # q4
        ("q4", "U"): ("qreject", "U", "R"),
        ("q4", "X"): ("q4", "X", "R"),
        ("q4", "0"): ("q3", "X", "R"),
        # q5
        ("q5", "U"): ("q2", "U", "R"),
        ("q5", "X"): ("q5", "X", "L"),
        ("q5", "0"): ("q5", "0", "L"),
    }
    current_state = "q1"

    # initiate the tape with the string surrounded by empty symbols
    tape = ["U"] + list(input_string) + ["U"]
    head_position = 1  # start of the input string

    # main loop
    while True:
        # index into delta to get the next state, the symbol to write/replace, and the direction on the tape to move
        next_state, write_symbol, move_direction = delta[
            (current_state, tape[head_position])
        ]

        # write the symbol
        tape[head_position] = write_symbol

        # change the state
        current_state = next_state

        # move along the tape
        if move_direction == "L":
            head_position -= 1
        elif move_direction == "R":
            head_position += 1

        # check for accept state
        if current_state in {"qaccept"}:
            print("Accept")
            break

        # also check for reject state
        if current_state in {"qreject"}:
            print("Reject")
            break


if __name__ == "__main__":
    # do stuff
    while True:
        user_input = input()
        run(user_input)
        if user_input == "quit":
            break
