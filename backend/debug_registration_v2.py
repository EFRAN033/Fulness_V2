import sys
import traceback
from app import models, schemas, utils, database
from app.database import SessionLocal

try:
    print("Creating database session...")
    db = SessionLocal()

    print("Hashing password...")
    hashed = utils.get_password_hash("securepassword123")

    print("Creating User object with new fields...")
    user = models.User(
        email="debug_patient@example.com",
        hashed_password=hashed,
        full_name="Debug User",
        identification="11223344",
        phone="555444333",
        role="paciente"
    )
    
    print("Checking for existing user...")
    existing = db.query(models.User).filter(models.User.email == "debug_patient@example.com").first()
    if existing:
        db.delete(existing)
        db.commit()

    print("Adding user to session...")
    db.add(user)
    print("Committing...")
    db.commit()
    print("User inserted.")
    
    db.refresh(user)
    print(f"User ID: {user.id}, Name: {user.full_name}, Role: {user.role}")

except Exception:
    traceback.print_exc()
finally:
    if 'db' in locals():
        db.close()
