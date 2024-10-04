
from Fleet import Fleet
from Reservation import Reservation


def print_menu():
    print(f"*** BORYS - RENT A CAR ***\n"
          f"1. Zarezerwuj samochód\n"
          f"2. Zwróć samochód\n"
          f"3. Nasza flota\n"
          f"4. Informacje o Twojej rezerwacji\n"
          f"5. Regulamin wypożyczalni 'BORYS'\n"
          f"6. Wyjście")
def main():
    try:
        while True:
            print_menu()
            user_choice = input("Choose an option: ")
            print()

            match user_choice:
                case '1':
                    pick_up_date = input("Enter pick-up date: ")
                    pick_up_time = input("Enter pick-up time: ")
                    return_date = input("Enter return date: ")
                    return_time = input("Enter return time: ")
                    pick_up_place = input("Enter pick-up place: ")
                    return_place = input("Enter return place: ")
                    new_reservation = Reservation(pick_up_date, pick_up_time,
                                                  return_date, return_time,
                                                  pick_up_place, return_place)
                    Reservation.create_and_add_new_reservation(new_reservation)



                case '3':
                    print("Our fleet:")
                    car_fleet = Fleet()
                    car_fleet.build_initial_fleet()
                    car_fleet.display_fleet()
                case '6':
                    exit()
                case _: # anything else
                    pass

    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
