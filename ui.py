from vehicle_management import MAIN_MENU_OPTIONS


def print_user_options():
    for i, option in enumerate(MAIN_MENU_OPTIONS, start=1):
        print(f"#{i} {option}")


def take_user_input() -> str:
    user_input = input("Please choose from one of the above options:\n")
    return user_input
