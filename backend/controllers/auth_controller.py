# backend/controllers/auth_controller.py
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import AuthService
from repos.customer_repo import CustomerRepository
from db.mongodb import get_database
from models.token import Token

router = APIRouter(prefix="/api", tags=["Authentication"])

# Dependency to inject the AuthService
def get_auth_service(db = Depends(get_database)):
    repo = CustomerRepository(db["customers"])
    return AuthService(repo)

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    auth_service: AuthService = Depends(get_auth_service)
):
    # The controller is now paper-thin!
    return await auth_service.authenticate_user(
        email=form_data.username, 
        password=form_data.password
    )