from models.reservation import Reservation
from config.db_config import get_db

class reservationView:
    def __init__(self,username=None, reservationId=None, number_of_seats=None, reservation_date=None):
        self.username = username
        self.reservationId = reservationId
        self.number_of_seats = number_of_seats
        self.reservation_date = reservation_date
        self.db = get_db()
    
    def insert(self):
        try:
            reservations_collection = self.db.reservations
            customers_collection = self.db.customers
            user = customers_collection.find_one({"username": self.username})
            reservation = Reservation(
            customerId = user["customerId"],
            reservationId = self.reservationId,
            number_of_seats = self.number_of_seats,
            reservation_date = self.reservation_date
            )
            result = reservations_collection.insert_one(reservation.to_dict())

            if result.inserted_id:
                return {"success": True, "message": "Reservation made successfully"}
            else:
                return {"success": False, "message": "Failed to add customer"}
        
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {e}"}
    
    def find(self):
        reservations_collection = self.db.reservations
        reservation_details = reservations_collection.find_one({"reservationId": self.reservationId})
        return reservation_details
