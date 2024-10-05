from DateValidator import DateValidator
from Fleet import Fleet
from Reservation import Reservation
from TimeValidator import TimeValidator
def print_menu():
    print(f"*** BORYS - RENT A CAR ***\n"
          f"1. Rent a car\n"
          f"2. Return car\n"
          f"3. Our fleet\n"
          f"4. Information about your reservation\n"
          f"5. Terms of use 'BORYS'\n"
          f"6. Exit")
def main():
    try:
        while True:
            print_menu()
            user_choice = input("Choose an option: ")

            match user_choice:
                case '1':
                    data_validator = DateValidator()
                    time_validator = TimeValidator()
                    while True:
                        pick_up_date = input("Enter pick-up date (DD-MM-YYYY): ")
                        if data_validator.is_valid_date(pick_up_date):
                            #print("The pick-up date is valid.")
                            break
                        else:
                            print("The pick-up date is invalid. Please enter a valid date in DD-MM-YYYY format.")

                    while True:
                        pick_up_time = input("Enter pick-up time (24h format): ")
                        if time_validator.is_valid_time(pick_up_time):
                            #print("The pick-up time is valid.")
                            break
                        else:
                            print("The pick-up time is invalid. Please enter a valid time format.")





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
