from fastapi import APIRouter, HTTPException
from models import User
from schemas import UserSchema

# Create a router for user routes
router = APIRouter()

# Create a new user
@router.post("/", response_model=dict)
def create_user(user: UserSchema):
    user_instance = User(**user.model_dump())
    user_id = user_instance.save()
    return {"id": str(user_id)}

# Get user details by user ID
@router.get("/{user_id}", response_model=dict)
def get_user(user_id: str):
    user = User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user['_id'] = str(user['_id'])
    return user
