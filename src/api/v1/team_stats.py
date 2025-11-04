from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.services.match_analysis import get_last_matches_for_team


router = APIRouter(prefix="/teams", tags=["Teams"])


def calculate_expected_goals(matches, team_id, home_advantage):
    pass


@router.get("/{team_id}/avg_goals")
async def avg_goals(team_id: int, last_n: int = 5, db: AsyncSession = Depends(get_db)):
    matches = await get_last_matches_for_team(db, team_id, last_n)
    avg_goals = calculate_expected_goals(matches, team_id=team_id, home_advantage=True)
    return {"team_id": team_id, "avg_goals": avg_goals}


@router.get("/{team_id}/performance_trend")
async def performance_trend(team_id: int, last_n: int = 10, db: AsyncSession = Depends(get_db)):
    matches = await get_last_matches_for_team(db, team_id, last_n)
    trend = []
    for m in matches[::-1]:
        if m.home_team_id == team_id:
            trend.append(m.home_score)
        else:
            trend.append(m.away_score)
    return {"team_id": team_id, "goals_trend": trend}
