from passlib.context import CryptContext
from sqlalchemy.orm import Session
from crud import get_user_by_email
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def authenticate_password(user_password,hashed_password):
    return pwd_context.verify(user_password,hashed_password)
def get_passowrd_hash(password):
    return pwd_context.hash(password)
    
def authenticate_user(db: Session,email: str,password: str):
    user=get_user_by_email(db,email=email)
    if not user:
        return False
    if not authenticate_password(password,user.password):
        return False
    return user