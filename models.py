from pymongo import MongoClient
from bson import ObjectId

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.expenses_db

# User model
class User:
    def __init__(self, email, name, mobile):
        self.email = email
        self.name = name
        self.mobile = mobile

    # Save user to database
    def save(self):
        return db.users.insert_one(self.__dict__).inserted_id

    # Get user by ID
    @staticmethod
    def get(user_id):
        return db.users.find_one({"_id": ObjectId(user_id)})

    # Get all users
    @staticmethod
    def get_all():
        return db.users.find()

# Expense model
class Expense:
    def __init__(self, payer_id, amount, split_type, splits):
        self.payer_id = payer_id
        self.amount = amount
        self.split_type = split_type
        self.splits = splits

    # Save expense to database
    def save(self):
        return db.expenses.insert_one(self.__dict__).inserted_id

    # Get expense by ID
    @staticmethod
    def get(expense_id):
        return db.expenses.find_one({"_id": ObjectId(expense_id)})

    # Get all expenses
    @staticmethod
    def get_all():
        return db.expenses.find()
