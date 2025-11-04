from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.league import League
from src.schema.league import LeagueCreate

async def create_league(db: AsyncSession, league: LeagueCreate):
    db_league = League(**league.dict())
    db.add(db_league)
    await db.commit()
    await db.refresh(db_league)
    return db_league

async def get_all_leagues(db: AsyncSession):
    result = await db.execute(select(League))
    return result.scalars().all()

async def get_league_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(League).where(League.name == name))
    return result.scalars().first()