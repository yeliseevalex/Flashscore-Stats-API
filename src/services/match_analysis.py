from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.models.match import Match

async def get_last_matches_for_team(db: AsyncSession, team_id: int, limit: int = 5):
    """Возвращает последние N матчей команды"""
    result = await db.execute(
        select(Match)
        .where((Match.home_team_id == team_id) | (Match.away_team_id == team_id))
        .order_by(Match.date.desc())
        .limit(limit)
    )
    return result.scalars().all()


async def get_last_matches_between_teams(db: AsyncSession, home_team_id: int, away_team_id: int, limit: int = 5):
    """Возвращает последние N матчей между двумя командами"""
    result = await db.execute(
        select(Match)
        .where(
            ((Match.home_team_id == home_team_id) & (Match.away_team_id == away_team_id)) |
            ((Match.home_team_id == away_team_id) & (Match.away_team_id == home_team_id))
        )
        .order_by(Match.date.desc())
        .limit(limit)
    )
    return result.scalars().all()
