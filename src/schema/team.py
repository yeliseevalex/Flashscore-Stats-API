from pydantic import BaseModel

class TeamBase(BaseModel):
    name: str | None = None
    country: str | None = None

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    id: int
    class Config:
        orm_mode = True
