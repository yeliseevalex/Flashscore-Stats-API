from sqlalchemy.ext.asyncio import AsyncSession
from src.services.match_analysis import get_last_matches_for_team, get_last_matches_between_teams
from src.services.score_prediction import calculate_expected_goals

async def predict_score(db: AsyncSession, home_team_id: int, away_team_id: int, last_n: int = 5):
    home_matches = await get_last_matches_for_team(db, home_team_id, limit=last_n)
    away_matches = await get_last_matches_for_team(db, away_team_id, limit=last_n)

    head_to_head = await get_last_matches_between_teams(db, home_team_id, away_team_id, limit=last_n)

    home_goals = calculate_expected_goals(home_matches, head_to_head, team_id=home_team_id, home_advantage=True)
    away_goals = calculate_expected_goals(away_matches, head_to_head, team_id=away_team_id, home_advantage=False)

    return {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "expected_score": f"{home_goals} - {away_goals}"
    }
