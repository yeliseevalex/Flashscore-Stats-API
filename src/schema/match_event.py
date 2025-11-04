from pydantic import BaseModel

class MatchEventBase(BaseModel):
    match_id: int | None = None
    minute: int | None = None
    event_type: str | None = None
    team_id: int | None = None
    player: str | None = None
    assist_player: str | None = None

class MatchEventCreate(MatchEventBase):
    pass

class MatchEventResponse(MatchEventBase):
    id: int
    class Config:
        orm_mode = True
