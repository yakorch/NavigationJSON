"""A module that navigates through a json file recieved from Twitter API"""
import argparse
import json


def reading_file(filename: str):
    """
    Returns a dictionary as result of reading a file 'filename'
    Args:
        filename (str): path to a file
    Returns:
        dict: a dictionary with info
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        info = json.load(file)
    return info


def nav_through(dct: dict, start_agian=None):
    """
    Navygating function.
    Works recusivly and gives user info about json file.
    Options for user: 'start again', 'exit' at any time
    Func helps going through file by showing hints.
    """
    if isinstance(dct, dict):
        print(f"You are in a dictionary. Possible keys: {list(dct.keys())}")
        user_input = input("Choose your option: ")
        while user_input not in dct.keys() and user_input not in (
                "start again", "exit"):
            print(
                f"You chose wrong key. Try again. Possible keys: {dct.keys()}")
            user_input = input("Choose your option: ")
        print()
        if user_input == "start again":
            return nav_through(dct=start_agian, start_agian=start_agian)
        elif user_input == "exit":
            return None
        return nav_through(dct[user_input], start_agian=start_agian)

    elif isinstance(dct, list):
        len_lst = len(dct)
        print(f"The len of a list you are in is {len_lst}")
        if len(dct) == 0:
            print("The list is empty")
            user_input = input("Write 'start again' or 'exit': ")
            while user_input not in ("start again", "exit"):
                user_input = input("Wrong one. Try again: ")
        else:
            print("Which element would you like to see?")
            user_input = input("Index of element: ")
            while user_input not in [
                    str(i) for i in range(len_lst)
            ] and user_input not in ("start again", "exit"):
                print("You chose wrong index. Try again.", end=" ")
                print(f"Possible choises: 0 - {len_lst - 1}")
                user_input = input("Index of element: ")
        print()
        if user_input == "start again":
            return nav_through(dct=start_agian, start_agian=start_agian)
        elif user_input == "exit":
            return None
        return nav_through(dct[int(user_input)], start_agian=start_agian)

    else:
        print(f"You are at: {dct}")
        print("If you want to start again then write 'start again'.", end=" ")
        print("Stop the program - 'exit'")
        user_input = input("Your choice: ")
        while user_input not in ("start again", "exit"):
            user_input = input("Wrong one. Try again: ")
        print()
        if user_input == 'start again':
            return nav_through(dct=start_agian, start_agian=start_agian)
        else:
            return None


def main():
    """
    Main function. Parses args, reads a file and starts a navigation.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_file', type=str, help='a path to a json file')
    args = parser.parse_args()
    file = args.path_to_file
    info_file = reading_file(file)
    print("At any point you can write 'start again' to start again")
    print("Also you can write 'exit' to finish a program")
    nav_through(info_file, info_file)


if __name__ == "__main__":
    main()
