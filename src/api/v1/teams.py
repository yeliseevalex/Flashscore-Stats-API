from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.team_repo import create_team, get_all_teams
from src.schema.team import TeamCreate, TeamResponse

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/", response_model=list[TeamResponse])
async def read_teams(db: AsyncSession = Depends(get_db)):
    return await get_all_teams(db)

@router.post("/", response_model=TeamResponse)
async def add_team(team: TeamCreate, db: AsyncSession = Depends(get_db)):
    return await create_team(db, team)
