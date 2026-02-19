from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Profile fields
    full_name = Column(String)
    identification = Column(String)  # DNI
    phone = Column(String)
    role = Column(String)  # 'paciente' or 'especialista'
    
    # Specialist fields
    medical_license = Column(String, nullable=True) # Num Colegiado
    specialty = Column(String, nullable=True)
