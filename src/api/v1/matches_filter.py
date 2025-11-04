from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.core.database import get_db
from src.models.match import Match

router = APIRouter(prefix="/matches", tags=["Matches"])

@router.get("/filter")
async def filter_matches(
    league_id: int | None = None,
    season: str | None = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Match)
    if league_id:
        query = query.where(Match.league_id == league_id)
    if season:
        query = query.where(Match.season == season)

    result = await db.execute(query)
    matches = result.scalars().all()

    return [
        {
            "match_id": m.id,
            "home_team_id": m.home_team_id,
            "away_team_id": m.away_team_id,
            "score": f"{m.home_score} - {m.away_score}",
            "date": m.date.isoformat(),
            "league_id": m.league_id,
            "season": m.season
        }
        for m in matches
    ]
