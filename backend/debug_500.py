import sys
import traceback

try:
    print("Importing modules...")
    from app import models, schemas, utils, database
    from app.database import SessionLocal, engine
    print("Modules imported.")

    print("Creating database session...")
    db = SessionLocal()
    print("Session created.")

    print("Testing password hashing...")
    pwd = "securepassword123"
    hashed = utils.get_password_hash(pwd)
    print(f"Password hashed: {hashed}")

    print("Testing Pydantic model...")
    user_data = schemas.UserCreate(email="test@example.com", password=pwd)
    print("Pydantic model created.")

    print("Testing database insertion...")
    user = models.User(email="test@example.com", hashed_password=hashed)
    # Check if exists
    existing = db.query(models.User).filter(models.User.email == "test@example.com").first()
    if existing:
        print("User already exists, deleting for test...")
        db.delete(existing)
        db.commit()
    
    db.add(user)
    db.commit()
    print("User inserted.")
    
    db.refresh(user)
    print(f"User ID: {user.id}")

except Exception:
    traceback.print_exc()
finally:
    if 'db' in locals():
        db.close()
