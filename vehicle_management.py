from sys import exit
from database import db, add_vehicle, get_database, delete_vehicle, update_vehicle, export_data
from typing import Tuple

MAIN_MENU_OPTIONS = (
    "Add vehicle to inventory",
    "Delete vehicle from inventory",
    "View current inventory",
    "Update vehicle",
    "Export current inventory",
    "Quit"
)


def map_user_input(user_input: int):
    if user_input == 1:
        vehicle_data = take_user_add_vehicle_input()
        # validate
        add_vehicle(*vehicle_data)
        print("Vehicle added successfully.")
        print()
    elif user_input == 2:
        try:
            _id = take_user_delete_vehicle_input()
            # validate
            delete_vehicle(_id)
            print("Vehicle deleted successfully.")
            print()
        except ValueError:
            print("Wrong input.")
    elif user_input == 3:
        print_inventory()
    elif user_input == 4:
        try:
            update_vehicle(*take_user_update_vehicle_input())
            print("Vehicle updated successfully.")
        except ValueError:
            print("Wrong id.")
        print()
    elif user_input == 5:
        export_data("data.csv")
        print("Data exported successfully")
        print()
    elif user_input == 6:
        exit(0)
    else:
        raise RuntimeError(f"Unknown main menu option {user_input}")


def take_user_add_vehicle_input() \
        -> Tuple[str, str, str, str, str]:
    make = input("Enter manufacturer: ")
    model = input("Enter model: ")
    year = input("Enter year: ")
    color = input("Enter color: ")
    range = input("Enter range: ")
    return make, model, year, color, range


def take_user_delete_vehicle_input() -> int:
    return int(input("Enter id:\n")) - 1


def take_user_update_vehicle_input() -> Tuple[int, str, str, str, str, str]:
    _id = take_user_delete_vehicle_input()
    vehicle_data = take_user_add_vehicle_input()
    return (_id,) + vehicle_data


def print_inventory():
    print("Car details:")
    for i, car_data in enumerate(get_database(), start=1):
        print(f"#{i} {car_data[0]} {car_data[1]} {car_data[2]} {car_data[3]} {car_data[4]}")
    print()
