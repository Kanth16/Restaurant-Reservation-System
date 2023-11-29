class Reservation:
    def __init__(self, customerId, reservationId, number_of_seats, reservation_date):
        self.customerId = customerId
        self.reservationId = reservationId
        self.number_of_seats = number_of_seats
        self.reservation_date = reservation_date

    def to_dict(self):
        return {
            "customerId": self.customerId,
            "reservationId": self.reservationId,
            "number_of_seats": self.number_of_seats,
            "reservation_date": self.reservation_date
        }
