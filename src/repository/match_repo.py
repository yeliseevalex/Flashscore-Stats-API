from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.match import Match
from src.schema.match import MatchCreate

async def create_match(db: AsyncSession, match: MatchCreate):
    db_match = Match(**match.dict())
    db.add(db_match)
    await db.commit()
    await db.refresh(db_match)
    return db_match

async def get_all_matches(db: AsyncSession):
    result = await db.execute(select(Match))
    return result.scalars().all()
