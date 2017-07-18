"""
Advent of code day four
Reference: https://adventofcode.com/2016/day/4
"""
import os
import operator

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',\
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def load_input_part_one(input_file):
    """
    Read from input file and parse them into tuple with format (name, sector_id, check_sum)
    """
    rooms = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        name = ''.join(line[:line.find('[')].split('-')[:-1])
        sector_id = int(line[:line.find('[')].split('-')[-1])
        check_sum = line[line.find('[') + 1:line.find(']')]
        rooms.append((name, sector_id, check_sum))
    return rooms

def part_one(rooms):
    """
    What is the sum of the sector IDs of the real rooms?
    """
    sector_id_sum = 0
    for room in rooms:
        letters = {}
        for item in room[0]:
            if item in letters:
                letters[item] += 1
            else:
                letters[item] = 1
        sorted_letters = sorted(letters.items(), key=operator.itemgetter(0))
        sorted_letters = sorted(sorted_letters, key=operator.itemgetter(1), reverse=True)
        count = 5
        most_common_letters = []
        for item in sorted_letters:
            if not most_common_letters or item[1] < most_common_letters[-1][-1][1] and count > 0:
                most_common_letters.append([item])
            elif item[1] == most_common_letters[-1][-1][1] and count > 0:
                most_common_letters[-1].append(item)
            count -= 1
        hierarchy = []
        for item in most_common_letters:
            hierarchy.append([x[0] for x in item])
        level = 0
        check_sum_letter_count = 0
        while check_sum_letter_count < len(room[2]) and level < len(hierarchy):
            if room[2][check_sum_letter_count] in hierarchy[level]:
                check_sum_letter_count += 1
            elif room[2][check_sum_letter_count] not in hierarchy[level]:
                level += 1
        if check_sum_letter_count == len(room[2]):
            sector_id_sum += room[1]
    return sector_id_sum

def load_input_part_two(input_file):
    """
    Read from input file and parse them into tuple with format (name, sector_id, check_sum)
    """
    rooms = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        content = opened_file.readlines()
    for line in content:
        name = line[:line.rfind('-')]
        sector_id = int(line[:line.find('[')].split('-')[-1])
        check_sum = line[line.find('[') + 1:line.find(']')]
        rooms.append((name, sector_id, check_sum))
    return rooms

def part_two(rooms):
    """
    What is the sector ID of the room where North Pole objects are stored?
    """
    for room in rooms:
        name = ""
        for letter in room[0]:
            if letter == '-':
                name += " "
            else:
                name += LETTERS[(LETTERS.index(letter) + room[1]) % 26]
        if name == "northpole object storage":
            return room[1]

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    rooms = load_input_part_one(current_file + INPUT_FILE_EXTENSION)
    print "Part one answer:", part_one(rooms)
    rooms = load_input_part_two(current_file + INPUT_FILE_EXTENSION)
    print "Part one answer:", part_two(rooms)

if __name__ == "__main__":
    main()
