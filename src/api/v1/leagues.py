from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.league_repo import create_league, get_all_leagues
from src.schema.league import LeagueCreate, LeagueResponse

router = APIRouter(prefix="/leagues", tags=["Leagues"])

@router.get("/", response_model=list[LeagueResponse])
async def read_leagues(db: AsyncSession = Depends(get_db)):
    return await get_all_leagues(db)

@router.post("/", response_model=LeagueResponse)
async def add_league(league: LeagueCreate, db: AsyncSession = Depends(get_db)):
    return await create_league(db, league)
