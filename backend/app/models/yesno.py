from sqlmodel import Field, SQLModel

class YesNo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    timestamp: str
    answer: str