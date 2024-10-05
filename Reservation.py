class Reservation:
    reservations = []

    def __init__(self, pick_up_date, pick_up_time, return_date, return_time, pick_up_place, return_place):
        self.pick_up_date = pick_up_date
        self.pick_up_time = pick_up_time
        self.return_date = return_date
        self.return_time = return_time
        self.pick_up_place = pick_up_place
        self.return_place = return_place

    def __str__(self):
        return (f"Pick-Up date: {self.pick_up_date}"
                f"Pick-Up time: {self.pick_up_time}"
                f"Return date: {self.return_date}"
                f"Return time: {self.return_time}"
                f"Pick-Up place: {self.return_place}"
                f"Return place: {self.return_place}")

    def create_and_add_new_reservation(self):
        new_reservation = Reservation(self.pick_up_date, self.pick_up_time,
                                      self.return_date, self.return_time,
                                      self.pick_up_place, self.return_place)
        Reservation.reservations.append(new_reservation)


    def add_reservation(self, book):
        self.reservations.append(book)
