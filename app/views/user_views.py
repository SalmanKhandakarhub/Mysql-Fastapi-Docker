from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import AsyncGenerator, Annotated
from jose import JWTError
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from ..schemas import user_schemas
from ..crud import user_crud
from ..models.database import AsyncSession, AsyncSessionLocal
from ..core.security import verify_password, create_access_tocken, verify_access_token
from app.models.models import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login/")
        
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        # print(type(session))
        yield session

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = verify_access_token(token, credentials_exception)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        
        result = await db.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()
        
        if user is None:
            raise credentials_exception

        return user
    except JWTError:
        raise credentials_exception
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= str(e)
        )

@router.post("/register/", response_model=user_schemas.RegisterResponse)
async def register_user(user: user_schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        existing_user = await user_crud.get_email(db, user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Email is already registered"
                )
        
        created_user = await user_crud.create_user(db=db, user=user)
        user_data = user_schemas.UserResponseData.from_orm(created_user)
        return {
            "message": "Registration successfully",
            "data": user_data
        }
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
            )
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
            )
    
@router.post("/login/", response_model=user_schemas.LoginSuccessResponse) #if hide this api  "include_in_schema=False"
async def login_user(user: OAuth2PasswordRequestForm = Depends(), db : AsyncSession=Depends(get_db)):
    try:
        print("hello")
        user_data = await user_crud.get_user_by_email(db, user.username)
        if not user_data or not verify_password(user.password, user_data.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"}
                )
            
        access_token = create_access_tocken(data={"sub": user_data.email})
        return{
            "message": "Login successfully",
            "access_token": access_token,
            "token_type": "bearer"
        }
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
            )
        
@router.get("/get_all_users/", response_model=user_schemas.GetAllUserResponse)
async def get_users(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        # print(current_user.type)
        # if current_user.type != "admin":
        #     raise HTTPException(
        #         status_code=status.HTTP_403_FORBIDDEN,
        #         detail="Not enough permissions"
        #     )
        users = await user_crud.get_all_user(db)
        user_data = [user_schemas.UserResponseData.from_orm(user) for user in users]
        return {
            "message": "Users fetched successfully",
            "data": user_data
        }
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )