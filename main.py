import sys
from car_database import Fleet
def print_menu():
    print(f"*** BORYS - RENT A CAR ***\n"
          f"1. Zarezerwuj samochód\n"
          f"2. Zwróć samochód\n"
          f"3. Nasza flota\n"
          f"4. Informacje o Twojej rezerwacji\n"
          f"5. Regulamin wypożyczalni 'BORYS'\n"
          f"6. Wyjście")
try:
    while True:
        print_menu()
        user_choice = input("Choose an option: \n")
        if user_choice == '1':
            pass
        elif user_choice == '2':
            pass
        elif user_choice == '3':
            car_fleet = Fleet()
            car_fleet.add_fleet()
            car_fleet.display_fleet()
        elif user_choice == '4':
            pass
        elif user_choice == '5':
            pass
        elif user_choice == '6':
            sys.exit()
        else:
            print("Invalid choice.")
except KeyboardInterrupt:
    print("Exiting...")
