from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.match_repo import create_match, get_all_matches
from src.schema.match import MatchCreate, MatchResponse

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.get("/", response_model=list[MatchResponse])
async def read_matches(db: AsyncSession = Depends(get_db)):
    return await get_all_matches(db)

@router.post("/", response_model=MatchResponse)
async def add_match(match: MatchCreate, db: AsyncSession = Depends(get_db)):
    return await create_match(db, match)
