import sys
import prints


def choose_modul():
    inputs = prints.input_handling(["Choose an option: "], "")
    option = inputs[0]
    if option == "1":
        quote.daily_quote()
    elif option == "2":
        skill.start_modul()
    elif option == "3":
        statitstics.start_modul()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("No such options")


def menu_handing():
    options = ["My daily quote", "Acces skill tree", "Show my statistics"]
    prints.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        menu_handing()
        try:
            choose_modul()
        except KeyError:
            print("No such option")


if __name__ == "__main__":
    main()
