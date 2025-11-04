from pydantic import BaseModel

class LeagueBase(BaseModel):
    name: str | None = None
    country: str | None = None

class LeagueCreate(LeagueBase):
    pass

class LeagueResponse(LeagueBase):
    id: int
    class Config:
        orm_mode = True
