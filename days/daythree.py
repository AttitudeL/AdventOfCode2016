"""
Advent of code day three
Reference: https://adventofcode.com/2016/day/3
"""
import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    """
    Read from input file and parse them into list of digits with group of size 3
    """
    digits = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        digits.append([int(x.strip()) for x in line.split()])
    return digits

def validate_triangle(le1, le2, le3):
    """
    Validate triangle given the length of its three sides
    """
    return le1 + le2 > le3 and le1 + le3 > le2 and le2 + le3 > le1

def part_one(digits):
    """
    In your puzzle input, how many of the listed triangles are possible?
    """
    valid_triangles = 0
    for group in digits:
        if validate_triangle(group[0], group[1], group[2]):
            valid_triangles += 1
    return valid_triangles

def part_two(digits):
    """
    Triangles are grouped into set of three vertically, calculate the possible triangles
    """
    vertical_digits = []
    for i in range(3):
        for group in digits:
            vertical_digits.append(group[i])
    triangles = [vertical_digits[x:x+3] for x in xrange(0, len(vertical_digits), 3)]
    valid_triangles = 0
    for triangle in triangles:
        if validate_triangle(triangle[0], triangle[1], triangle[2]):
            valid_triangles += 1
    return valid_triangles

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    digits = load_input(current_file + INPUT_FILE_EXTENSION)
    print "Part one answer:", part_one(digits)
    print "Part one answer:", part_two(digits)

if __name__ == "__main__":
    main()
