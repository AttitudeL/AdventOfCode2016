"""
Advent of code day six
Reference: https://adventofcode.com/2016/day/6
"""
import os

INPUT_DIRECTORY = "../inputs/"
INPUT_FILE_EXTENSION = "_input.txt"

def load_input(input_file):
    """
    Read from input file
    """
    messages = []
    relative_path = os.path.join(os.path.dirname(__file__), INPUT_DIRECTORY + input_file)
    with open(relative_path, 'r') as opened_file:
        lines = opened_file.readlines()
    for line in lines:
        for index, letter in enumerate(line.strip()):
            if len(messages) < index + 1:
                messages.append([letter])
            else:
                messages[index].append(letter)
    return messages

def part_one(messages):
    """
    What is the error-corrected version of the message being sent?
    """
    occurrences = []
    for message in messages:
        occurrence = {}
        for letter in message:
            if letter in occurrence:
                occurrence[letter] += 1
            else:
                occurrence[letter] = 1
        occurrences.append(occurrence)
    error_corrected_message = ""
    for occurrence in occurrences:
        count = 0
        for key in occurrence:
            count = max(occurrence[key], count)
        for key in occurrence:
            if occurrence[key] == count:
                error_corrected_message += key
    return error_corrected_message

def main():
    """
    Main function
    """
    current_file = os.path.splitext(os.path.basename(__file__))[0]
    messages = load_input(current_file + INPUT_FILE_EXTENSION)
    #print messages
    print "Part one answer:", part_one(messages)
    #print "Part two answer:", part_two(door_id)

if __name__ == "__main__":
    main()
