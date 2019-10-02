import os


def input_handling(list_labels, title):
    inputs = []

    print(f"\n{title}")

    for label in list_labels:
        inputs.append(input(label + " "))
    return inputs


def print_menu(title, menu_options, exit_msg):
    if title == "Main menu":
        os.system('clear')
    print(title + ":")
    for index in range(len(menu_options)):
        print("\t" + f"({index + 1}) {menu_options[index]}")
    print("\t" + f"({0}) {exit_msg}")


def print_results(result, label):
    
