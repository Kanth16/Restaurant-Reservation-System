from models.customer import Customer
from models.reservation import Reservation
from config.db_config import get_db

class adminView:
    def __init__(self):
        self.db = get_db()
        self.customers=self.db.customers
        self.reservations = self.db.reservations
    
    def adminData(self):
        customers_collection = self.customers
        reservations_collection = self.reservations
        
        customers = list(customers_collection.find())
        customer_reservations = []

        for customer in customers:
            # Find all reservations for this customer
            reservations = list(reservations_collection.find({"customerId": customer["customerId"]}))
            customer_data = {
                "username": customer["username"],
                "name": customer.get("name", ""),
                "email": customer.get("email", ""),
                "reservations": reservations
            }
            customer_reservations.append(customer_data)
        return customer_reservations