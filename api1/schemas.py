from pydantic import BaseModel


class NewStudent(BaseModel):
    StdNo: str
    FirstName: str
    LastName: str
    FatherName: str = None
    BirthDate: str = None
    Average: float = None
    Gender: int = None
    CityID: int
