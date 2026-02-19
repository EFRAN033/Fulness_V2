from app import models, database
from app.database import engine

print("Dropping tables...")
models.Base.metadata.drop_all(bind=engine)
print("Creating tables...")
models.Base.metadata.create_all(bind=engine)
print("Database reset complete.")
