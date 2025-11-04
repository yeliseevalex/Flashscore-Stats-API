from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.database import get_db
from src.models.match import Match
from src.models.match_event import MatchEvent
from src.models.team import Team

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/goals_by_minute/{team_id}")
async def goals_by_minute(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MatchEvent).where(
        MatchEvent.team_id == team_id,
        MatchEvent.event_type == "goal"
    ))
    events = result.scalars().all()

    stats = {}
    for e in events:
        minute = e.minute
        stats[minute] = stats.get(minute, 0) + 1

    return {"team_id": team_id, "goals_by_minute": stats}


@router.get("/cards_by_minute/{team_id}")
async def cards_by_minute(team_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MatchEvent).where(
        MatchEvent.team_id == team_id,
        MatchEvent.event_type.in_(["yellow_card", "red_card"])
    ))
    events = result.scalars().all()

    stats = {}
    for e in events:
        minute = e.minute
        stats[minute] = stats.get(minute, {"yellow": 0, "red": 0})
        if e.event_type == "yellow_card":
            stats[minute]["yellow"] += 1
        else:
            stats[minute]["red"] += 1

    return {"team_id": team_id, "cards_by_minute": stats}
