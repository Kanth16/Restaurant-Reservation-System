from models.customer import Customer
from config.db_config import get_db

class customerView:
    def __init__(self,customerId=None,username=None,name=None,address=None,phoneNumber=None,email=None):
        self.customerId=customerId
        self.username=username
        self.name=name
        self.address=address
        self.phoneNumber=phoneNumber
        self.email=email
        self.db = get_db()
    
    def insert(self):
        try:
            customers_collection = self.db.customers
            customer = Customer(
                customerId=self.customerId,
                username=self.username,
                name=self.name,
                address=self.address,
                phoneNumber=self.phoneNumber,
                email=self.email
            )

            result = customers_collection.insert_one(customer.to_dict())

            if result.inserted_id:
                return {"success": True, "message": "Customer added successfully"}
            else:
                return {"success": False, "message": "Failed to add customer"}
        
        except Exception as e:
            # Handle any exceptions that occur during the insert
            return {"success": False, "message": f"An error occurred: {e}"}
    
    def find(self):
        customers_collection = self.db.customers
        user = customers_collection.find_one({"username": self.username})
        return user
