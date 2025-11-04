from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.match_event import MatchEvent
from src.schema.match_event import MatchEventCreate

async def create_match_event(db: AsyncSession, event: MatchEventCreate):
    db_event = MatchEvent(**event.dict())
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event

async def get_events_by_match(db: AsyncSession, match_id: int):
    result = await db.execute(select(MatchEvent).where(MatchEvent.match_id == match_id))
    return result.scalars().all()
