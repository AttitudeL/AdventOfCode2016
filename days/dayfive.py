"""
Advent of code day five
Reference: https://adventofcode.com/2016/day/5
"""
import os
import md5

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    """
    Read from input file
    """
    door_id = ""
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        door_id = opened_file.read()
    return door_id

def part_one(door_id):
    """
    Given the actual Door ID, what is the password?
    """
    index = 0
    password = ""
    while len(password) < 8:
        md5_hash = md5.new()
        md5_hash.update(door_id + str(index))
        hex_val = md5_hash.hexdigest()
        if hex_val[:5] == "00000":
            password += hex_val[5]
        index += 1
    return password

def part_two(door_id):
    """
    Your puzzle input is still ffykfhsq.
    """
    index = 0
    password = [None, None, None, None, None, None, None, None]
    while None in password:
        md5_hash = md5.new()
        md5_hash.update(door_id + str(index))
        hex_val = md5_hash.hexdigest()
        if hex_val[:5] == "00000":
            position = int(hex_val[5], 16)
            if position >= 0 and position <= 7 and password[position] is None:
                password[position] = hex_val[6]
        index += 1
    return ''.join(password)

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    door_id = load_input(current_file + INPUT_FILE_EXTENSION)
    print "Part one answer:", part_one(door_id)
    print "Part two answer:", part_two(door_id)

if __name__ == "__main__":
    main()
    