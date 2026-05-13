class CustomerRepository:
    # Take in a mock database. Can be replaced with a real database later
    def __init__(self, db_customers: list):
        self.db = db_customers

    # Define functions that just retrive data from database. Don't care about rules.

    def get_all_customer(self):
        return self.db

    def get_id_customer(self, id : int):
        for cust in self.db:
            if id == cust.id:
                return cust
        
        return None
        