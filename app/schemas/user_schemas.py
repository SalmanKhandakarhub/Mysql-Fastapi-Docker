from pydantic import BaseModel, Field, EmailStr, validator
from typing import List
import re

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    confirm_password: str
    type: str
    
    @validator('password')
    def validate_password(cls, password):
        if not re.search(r'[A-Z]', password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r'[!@#$%^&*]', password):
            raise ValueError("Password must contain at least one special character")
        return password
    
    @validator('confirm_password')
    def password_match(cls, confirm_password, values):
        password = values.get('password')
        if password != confirm_password:
            raise ValueError("Password do not metch")
        return confirm_password
    
class UserCreate(UserBase):
    pass

class User(UserBase):
    id : int
    
    class Config:
        orm_mode = True
        from_attributes = True
        
# Response for register     
class UserResponseData(BaseModel):
    id: int
    name: str
    email: EmailStr
    type: str

    class Config:
        orm_mode = True
        from_attributes = True
        
class RegisterResponse(BaseModel):
    message: str
    data: UserResponseData

# Response for Login          
class LoginSuccessResponse(BaseModel):
    message: str
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
        
#Response for get all user
class GetAllUserResponse(BaseModel):
    message: str
    data: List[UserResponseData]