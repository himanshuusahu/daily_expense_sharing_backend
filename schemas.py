from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator
from typing import List, Optional

# Schema for user data validation
class UserSchema(BaseModel):
    email: EmailStr
    name: str
    mobile: str

# Schema for split data validation
class SplitSchema(BaseModel):
    user_id: str
    amount: Optional[float]
    percentage: Optional[float]

# Schema for expense data validation
class ExpenseSchema(BaseModel):
    payer_id: str
    amount: float
    split_type: str
    splits: List[SplitSchema]

    # Validate that percentages add up to 100% in percentage split
    @field_validator('splits')
    def validate_splits(cls, splits, values):
        split_type = values.get('split_type')
        if split_type == 'percentage':
            total_percentage = sum([split.percentage for split in splits if split.percentage])
            if total_percentage != 100:
                raise ValueError('Percentages must add up to 100')
        return splits
