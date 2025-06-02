from guesser import guess

def handle_option(selected_option, options):
    if selected_option == 0:
        print("Bye!")
        return True
    else:
        match selected_option:
            case 1:
                guess()
            case _:
                print("Uh-oh this option doesn't exist, try again!")

        return False
    
def get_selected_option(options):
    while True:
        try:
            return int(input("Select one option: "))
        except ValueError:
            print("No, no, no, you need to use the numbers to navigate")

def show_menu(options):
    for option in options:
        print(f"{option}")
    
def main():
    options = ["1 - Listen and guess", "0 - Exit"]
    while True:
        show_menu(options)
        selected_option = get_selected_option(options)

        if handle_option(selected_option, options):
            break

if __name__ == "__main__":
    main()