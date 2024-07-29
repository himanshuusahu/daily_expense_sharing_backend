from fastapi import FastAPI
from pymongo import MongoClient
from routes.user_routes import router as user_router  # Import user routes
from routes.expense_routes import router as expense_router  # Import expense routes

# Create a FastAPI app instance
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.expenses_db

# Include user and expense routers with prefixes
app.include_router(user_router, prefix="/users")
app.include_router(expense_router, prefix="/expenses")

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=3001)
