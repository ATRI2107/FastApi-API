from passlib.context import CryptContext
from sqlalchemy.orm import Session

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def authenticate_password(user_password,hashed_password):
    return pwd_context.verify(user_password,hashed_password)
def get_passowrd_hash(password):
    return pwd_context.hash(password)
