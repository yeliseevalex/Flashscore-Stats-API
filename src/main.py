from fastapi import FastAPI
from core.database import Base, engine
from api.v1 import leagues, matches, match_events, teams, prediction, analytics, matches_filter, team_stats

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(leagues.router)
app.include_router(matches.router)
app.include_router(match_events.router)
app.include_router(teams.router)
app.include_router(prediction.router)
app.include_router(analytics.router)
app.include_router(matches_filter.router)
app.include_router(team_stats.router)