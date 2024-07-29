from fastapi import APIRouter, HTTPException
from models import Expense, User
from schemas import ExpenseSchema
from utils import calculate_splits

# Create a router for expense routes
router = APIRouter()

# Add a new expense
@router.post("/addExpense", response_model=dict)
def add_expense(expense: ExpenseSchema):
    data = calculate_splits(expense.dict())
    expense_instance = Expense(**data)
    expense_id = expense_instance.save()
    return {"id": str(expense_id)}

# Get expense details by expense ID
@router.get("/{expense_id}", response_model=dict)
def get_expense(expense_id: str):
    expense = Expense.get(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense['_id'] = str(expense['_id'])
    return expense

# Get the balance sheet for all users
@router.get("/balance_sheet", response_model=dict)
def get_balance_sheet():
    users = list(User.get_all())
    expenses = list(Expense.get_all())
    balance_sheet = {}
    for user in users:
        balance_sheet[str(user['_id'])] = {"name": user['name'], "balance": 0}

    for expense in expenses:
        payer_id = expense['payer_id']
        balance_sheet[payer_id]['balance'] += expense['amount']
        for split in expense['splits']:
            user_id = split['user_id']
            balance_sheet[user_id]['balance'] -= split['amount']

    return balance_sheet
