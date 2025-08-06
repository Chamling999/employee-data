from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------------
# Database Configuration
# ---------------------------
DATABASE_URL = "sqlite:///./employees.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


# ---------------------------
# SQLAlchemy Employee Model
# ---------------------------
class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)


# Create the table
Base.metadata.create_all(bind=engine)


# ---------------------------
# Pydantic Schemas
# ---------------------------
class EmployeeCreate(BaseModel):
    name: str
    age: int
    department: str


class EmployeeUpdate(BaseModel):
    name: str
    age: int
    department: str


# ---------------------------
# FastAPI App
# ---------------------------
app = FastAPI(title="Employee Data Management API")

# ---------------------------
# CRUD Routes
# ---------------------------


# Create a new employee
@app.post("/employees/", response_model=dict)
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()
    new_emp = Employee(**employee.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    db.close()
    return {
        "message": "Employee created successfully",
        "employee": {
            "id": new_emp.id,
            "name": new_emp.name,
            "age": new_emp.age,
            "department": new_emp.department,
        },
    }


# Read all employees
@app.get("/employees/", response_model=list)
def read_employees():
    db = SessionLocal()
    employees = db.query(Employee).all()
    result = [
        {"id": emp.id, "name": emp.name, "age": emp.age, "department": emp.department}
        for emp in employees
    ]
    db.close()
    return result


# Read a specific employee
@app.get("/employees/{employee_id}", response_model=dict)
def read_employee(employee_id: int):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    db.close()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {
        "id": emp.id,
        "name": emp.name,
        "age": emp.age,
        "department": emp.department,
    }


# Update an existing employee
@app.put("/employees/{employee_id}", response_model=dict)
def update_employee(employee_id: int, updated: EmployeeUpdate):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    for key, value in updated.dict().items():
        setattr(emp, key, value)
    db.commit()
    db.refresh(emp)
    db.close()
    return {
        "message": "Employee updated successfully",
        "employee": {
            "id": emp.id,
            "name": emp.name,
            "age": emp.age,
            "department": emp.department,
        },
    }


# Delete an employee
@app.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int):
    db = SessionLocal()
    emp = db.query(Employee).filter(Employee.id == employee_id).first()
    if not emp:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    db.close()
    return {"message": "Employee deleted successfully"}
