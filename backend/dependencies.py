# backend/dependencies.py
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from utils.auth import SECRET_KEY, ALGORITHM
from models.token import TokenData
from controllers.customer_controller import get_customer_service
from services.customer_service import CustomerService
from models.customer import CustomerResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme), 
    cust_service: CustomerService = Depends(get_customer_service)
) -> CustomerResponse:
    
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception

    # Fetch the user using the CustomerService
    user = await cust_service.getCustomerByID(token_data.user_id)
    if user is None:
        raise credentials_exception
        
    return user