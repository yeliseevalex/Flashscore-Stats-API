from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.team import Team
from src.schema.team import TeamCreate

async def create_team(db: AsyncSession, team: TeamCreate):
    db_team = Team(**team.dict())
    db.add(db_team)
    await db.commit()
    await db.refresh(db_team)
    return db_team

async def get_all_teams(db: AsyncSession):
    result = await db.execute(select(Team))
    return result.scalars().all()

async def get_team_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Team).where(Team.name == name))
    return result.scalars().first()
