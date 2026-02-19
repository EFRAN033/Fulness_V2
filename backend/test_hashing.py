from passlib.context import CryptContext
try:
    import bcrypt
    print(f"bcrypt version: {bcrypt.__version__}")
except ImportError:
    print("bcrypt not installed")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

try:
    print("Hashing 'test'...")
    hashed = pwd_context.hash("test")
    print(f"Hashed: {hashed}")
except Exception as e:
    print(f"Error: {e}")
