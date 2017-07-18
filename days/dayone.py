"""
Advent of code day one
Reference: https://adventofcode.com/2016/day/1
"""
import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

DIRECTIONS = ['N']

COORDINATE = [(0, 0)]

DIRECTION_ROTATION = {
    'N' : {
        'R' : 'E',
        'L' : 'W'
    },
    'E' : {
        'R' : 'S',
        'L' : 'N'
    },
    'S' : {
        'R' : 'W',
        'L' : 'E'
    },
    'W' : {
        'R' : 'N',
        'L' : 'S'
    }
}

def load_input(input_file):
    """
    Read from input file and parse them into individual instructions
    """
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        instructions = opened_file.read()
    return [x.strip() for x in instructions.split(',')]

def read_instruction(turn, blocks):
    """
    Generate the new direction and coordinate given the trun instruction and distance
    """
    previous_direction = DIRECTIONS[-1]
    current_direction = DIRECTION_ROTATION[previous_direction][turn]
    DIRECTIONS.append(current_direction)
    x_val = COORDINATE[-1][0]
    y_val = COORDINATE[-1][1]
    if current_direction == 'N':
        positive_y_coordinate(COORDINATE, x_val, y_val, blocks)
    elif current_direction == 'E':
        positive_x_coordinate(COORDINATE, x_val, y_val, blocks)
    elif current_direction == 'S':
        negative_y_coordinate(COORDINATE, x_val, y_val, blocks)
    elif current_direction == 'W':
        negative_x_coordinate(COORDINATE, x_val, y_val, blocks)

def positive_x_coordinate(coordinates, x_val, y_val, blocks):
    """
    Construct positive progressive coordinate for x axis
    """
    i = 1
    while x_val + i <= x_val + blocks:
        coordinates.append((x_val + i, y_val))
        i += 1

def negative_x_coordinate(coordinates, x_val, y_val, blocks):
    """
    Construct negative progressive coordinate for x axis
    """
    i = 1
    while x_val - i >= x_val - blocks:
        coordinates.append((x_val - i, y_val))
        i += 1

def positive_y_coordinate(coordinates, x_val, y_val, blocks):
    """
    Construct positive progressive coordinate for y axis
    """
    i = 1
    while y_val + i <= y_val + blocks:
        coordinates.append((x_val, y_val + i))
        i += 1

def negative_y_coordinate(coordinates, x_val, y_val, blocks):
    """
    Construct negative progressive coordinate for y axis
    """
    i = 1
    while y_val - i >= y_val - blocks:
        coordinates.append((x_val, y_val - i))
        i += 1

def read_instructions(instructions):
    """
    Read each instruction and generate direction and coordinate lists
    """
    for instruction in instructions:
        turn = instruction[:1]
        distance = int(instruction[1:])
        read_instruction(turn, distance)

def part_one():
    """
    How many blocks away is Easter Bunny HQ?
    """
    return abs(COORDINATE[-1][0]) + abs(COORDINATE[-1][1])

def part_two():
    """
    How many blocks away is the first location you visit twice?
    """
    coordinates = []
    for coordinate in COORDINATE:
        if coordinate in coordinates:
            return abs(coordinate[0]) + abs(coordinate[1])
        else:
            coordinates.append(coordinate)

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    instructions = load_input(current_file + INPUT_FILE_EXTENSION)
    read_instructions(instructions)
    print "Part one answer:", part_one()
    print "Part two answer:", part_two()

if __name__ == "__main__":
    main()
