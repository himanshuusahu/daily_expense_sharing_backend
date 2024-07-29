
# Daily Expenses Sharing Application

This project is a backend service for a daily-expenses sharing application built using FastAPI and MongoDB. The application allows users to add expenses and split them based on three different methods: exact amounts, percentages, and equal splits. It also provides user management and validation, as well as the ability to generate downloadable balance sheets.

## Features
- **User Management**: Add and retrieve user details.
- **Expense Management**: Add expenses and split them using different methods.
- **Balance Sheet**: Show individual and overall expenses for all users and provide a downloadable balance sheet.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/himanshuusahu/daily_expense_sharing_backend.git
    cd daily_expense_sharing_backend
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    or
    pip install fastapi uvicorn pymongo pydantic

    ```

4. **Start MongoDB:**
    Make sure you have MongoDB installed and running on your local machine. By default, the application connects to `mongodb://localhost:27017/`.

5. **Run the application:**
    ```bash
    uvicorn app:app --reload
    ```

## Endpoints

### User Endpoints

#### Create User
- **URL**: `/users/`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "email": "user@example.com",
        "name": "John Doe",
        "mobile": "1234567890"
    }
    ```
- **Response**:
    ```json
    {
        "id": "60f8a1c8b6e4a5d5f2a0e4d2"
    }
    ```

#### Get User Details
- **URL**: `/users/{user_id}`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "_id": "60f8a1c8b6e4a5d5f2a0e4d2",
        "email": "user@example.com",
        "name": "John Doe",
        "mobile": "1234567890"
    }
    ```

### Expense Endpoints

#### Add Expense
- **URL**: `/expenses/addExpense`
- **Method**: `POST`
- **Request Body**:
    ```json
    {
        "payer_id": "60f8a1c8b6e4a5d5f2a0e4d2",
        "amount": 3000.0,
        "split_type": "equal",
        "splits": [
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d2"
            },
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d3"
            },
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d4"
            }
        ]
    }
    ```
- **Response**:
    ```json
    {
        "id": "60f8a1c8b6e4a5d5f2a0e4d5"
    }
    ```

#### Get Expense Details
- **URL**: `/expenses/{expense_id}`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "_id": "60f8a1c8b6e4a5d5f2a0e4d5",
        "payer_id": "60f8a1c8b6e4a5d5f2a0e4d2",
        "amount": 3000.0,
        "split_type": "equal",
        "splits": [
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d2",
                "amount": 1000.0
            },
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d3",
                "amount": 1000.0
            },
            {
                "user_id": "60f8a1c8b6e4a5d5f2a0e4d4",
                "amount": 1000.0
            }
        ]
    }
    ```

#### Get Balance Sheet
- **URL**: `/expenses/balance_sheet`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "60f8a1c8b6e4a5d5f2a0e4d2": {
            "name": "John Doe",
            "balance": 0.0
        },
        "60f8a1c8b6e4a5d5f2a0e4d3": {
            "name": "Jane Doe",
            "balance": -1000.0
        },
        "60f8a1c8b6e4a5d5f2a0e4d4": {
            "name": "Sam Smith",
            "balance": -1000.0
        }
    }
    ```

## Project Structure

```
.
├── app.py                # Entry point of the application
├── models.py             # Data models for users and expenses
├── routes                # Directory for route definitions
│   ├── __init__.py       # Init file for routes package
│   ├── user_routes.py    # User routes
│   └── expense_routes.py # Expense routes
├── schemas.py            # Pydantic schemas for data validation
├── utils.py              # Utility functions
└── requirements.txt      # List of dependencies
```

## Utility Functions
- **calculate_splits**: Calculates the splits based on the split type (equal, exact, percentage).

### Example of `calculate_splits` in `utils.py`
```python
# Calculate splits based on split type
def calculate_splits(data):
    split_type = data['split_type']
    splits = data['splits']
    amount = data['amount']
    
    # Equal split
    if split_type == 'equal':
        split_amount = amount / len(splits)
        for split in splits:
            split['amount'] = split_amount
    
    # Exact split
    elif split_type == 'exact':
        for split in splits:
            if 'amount' not in split:
                raise ValueError('Exact split requires amount for each participant')
    
    # Percentage split
    elif split_type == 'percentage':
        for split in splits:
            if 'percentage' not in split:
                raise ValueError('Percentage split requires percentage for each participant')
            split['amount'] = (split['percentage'] / 100) * amount
    
    return data
```

