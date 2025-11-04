from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class MatchEvent(Base):
    __tablename__ = "match_events"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    minute = Column(Integer, nullable=False)
    event_type = Column(String, nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"))
    player = Column(String, nullable=False)
    assist_player = Column(String, nullable=True)

    match = relationship("Match")
    team = relationship("Team")
