from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base, Student
from schemas import NewStudent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

Base.metadata.create_all(bind=engine)


@app.get('/students')
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    if not students:
        raise HTTPException(status_code=404, detail='No students found.')
    return students


@app.post('/students')
def add_student(student: NewStudent, db: Session = Depends(get_db)):
    db_student = Student(
        StdNo=student.StdNo,
        FirstName=student.FirstName,
        LastName=student.LastName,
        FatherName=student.FatherName,
        BirthDate=student.BirthDate,
        Average=student.Average,
        Gender=student.Gender,
        CityID=student.CityID
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student
