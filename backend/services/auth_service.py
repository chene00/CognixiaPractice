from fastapi import HTTPException
from repos.customer_repo import CustomerRepository
from utils.auth import verify_password, create_access_token
from models.token import Token

class AuthService:
    def __init__(self, cust_repo: CustomerRepository):
        self.cust_repo = cust_repo

    async def authenticate_user(self, email: str, password: str) -> Token:
        # 1. Fetch user by email via Repo
        user = await self.cust_repo.get_customer_by_email(email)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        # 2. Verify password hash
        if not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        # 3. Assemble and return the token
        access_token = create_access_token(data={"sub": user.id})
        
        return Token(access_token=access_token, token_type="bearer")