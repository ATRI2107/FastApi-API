from sqlalchemy.orm import Session
from secure import get_passowrd_hash
import models
import schemas

def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()
def get_user_by_email(db: Session,email: str):
    return db.query(models.User).filter(models.User.email==email).first()
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password=get_passowrd_hash(user.password)
    db_user=models.User(email=user.email,password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db: Session,user_id: int):
    user=get_user(db,user_id)
    return user.items
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item=models.Item(**item.dict(),owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
