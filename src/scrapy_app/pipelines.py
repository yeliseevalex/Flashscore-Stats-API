import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db
from src.repository.team_repo import create_team, get_team_by_name
from src.repository.league_repo import create_league, get_league_by_name
from src.repository.match_repo import create_match
from src.schema.team import TeamCreate
from src.schema.league import LeagueCreate
from src.schema.match import MatchCreate

class FlashscorePipeline:
    """Асинхронное сохранение матчей, команд и лиг с проверкой существующих"""

    def __init__(self):
        self.loop = asyncio.get_event_loop()

    def process_item(self, item, spider):
        self.loop.run_until_complete(self.save_item(item))
        return item

    async def save_item(self, item):
        async with get_db() as db:

            # --- Сохраняем или получаем лигу ---
            league_name = item.get("league")
            league = await get_league_by_name(db, league_name)
            if not league:
                league_data = LeagueCreate(name=league_name)
                league = await create_league(db, league_data)

            # --- Сохраняем или получаем домашнюю команду ---
            home_team_name = item.get("home_team")
            home_team = await get_team_by_name(db, home_team_name)
            if not home_team:
                home_team = await create_team(db, TeamCreate(name=home_team_name))

            # --- Сохраняем или получаем гостевую команду ---
            away_team_name = item.get("away_team")
            away_team = await get_team_by_name(db, away_team_name)
            if not away_team:
                away_team = await create_team(db, TeamCreate(name=away_team_name))


            score_text = item.get("score", None)
            try:
                home_score, away_score = [int(x.strip()) for x in score_text.split("-")]
            except:
                home_score, away_score = None, None

            match_data = MatchCreate(
                league_id=league.id,
                home_team_id=home_team.id,
                away_team_id=away_team.id,
                home_score=home_score,
                away_score=away_score,
            )
            await create_match(db, match_data)
