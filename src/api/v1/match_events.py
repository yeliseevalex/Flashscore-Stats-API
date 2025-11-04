from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.match_event_repo import create_match_event, get_events_by_match
from src.schema.match_event import MatchEventCreate, MatchEventResponse

router = APIRouter(prefix="/match-events", tags=["Match Events"])

@router.get("/{match_id}", response_model=list[MatchEventResponse])
async def read_match_events(match_id: int, db: AsyncSession = Depends(get_db)):
    return await get_events_by_match(db, match_id)

@router.post("/", response_model=MatchEventResponse)
async def add_match_event(event: MatchEventCreate, db: AsyncSession = Depends(get_db)):
    return await create_match_event(db, event)
