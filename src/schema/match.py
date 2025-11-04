from datetime import datetime
from pydantic import BaseModel

class MatchBase(BaseModel):
    league_id: int | None = None
    home_team_id: int | None = None
    away_team_id: int | None = None
    date: datetime | None = None
    home_score: int | None = None
    away_score: int | None = None

class MatchCreate(MatchBase):
    pass

class MatchResponse(MatchBase):
    id: int
    class Config:
        orm_mode = True
