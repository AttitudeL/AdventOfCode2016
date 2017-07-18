"""
Advent of code day two
Reference: https://adventofcode.com/2016/day/2
"""
import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

KEYBOARD_PART_ONE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

KEYBOARD_PART_TWO = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None]
]

def load_input(input_file):
    """
    Read from input file and parse them into individual instructions
    """
    instructions = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        instructions.append(list(line.strip()))
    return instructions

def read_instruction(keyboard, keyboard_size, position, positions, direction):
    """
    Read from direction and add new position to the list
    """
    i = position[0]
    j = position[1]
    if direction == 'U':
        i = max(i - 1, 0)
    if direction == 'D':
        i = min(i + 1, keyboard_size)
    if direction == 'L':
        j = max(j - 1, 0)
    if direction == 'R':
        j = min(j + 1, keyboard_size)
    if keyboard[i][j] is None:
        positions.append((position[0], position[1]))
        return (position[0], position[1])
    else:
        positions.append((i, j))
        return (i, j)

def part_one(instructions, keyboard):
    """
    What is the bathroom code?
    """
    positions = []
    position = (1, 1)
    for instruction in instructions:
        partial = []
        for direction in instruction:
            position = read_instruction(KEYBOARD_PART_ONE, 2, position, partial, direction)
        positions.append(partial)
    code = ""
    for position in positions:
        code += str(keyboard[position[-1][0]][position[-1][1]])
    return code

def part_two(instructions, keyboard):
    """
    What is the bathroom code?
    """
    positions = []
    position = (2, 0)
    for instruction in instructions:
        partial = []
        for direction in instruction:
            position = read_instruction(KEYBOARD_PART_TWO, 4, position, partial, direction)
        positions.append(partial)
    code = ""
    for position in positions:
        code += str(keyboard[position[-1][0]][position[-1][1]])
    return code

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    instructions = load_input(current_file + INPUT_FILE_EXTENSION)
    print "Part one answer:", part_one(instructions, KEYBOARD_PART_ONE)
    print "Part two answer:", part_two(instructions, KEYBOARD_PART_TWO)

if __name__ == "__main__":
    main()
