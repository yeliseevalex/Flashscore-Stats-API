from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.match_analysis_repo import predict_score

router = APIRouter(prefix="/prediction", tags=["Prediction"])

@router.get("/{home_team_id}/{away_team_id}")
async def get_match_prediction(home_team_id: int, away_team_id: int, db: AsyncSession = Depends(get_db)):
    return await predict_score(db, home_team_id, away_team_id)
