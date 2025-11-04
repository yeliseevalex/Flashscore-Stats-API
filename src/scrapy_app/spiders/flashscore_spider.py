import scrapy
from src.scrapy_app.items import MatchItem, MatchEventItem

class FlashscoreSpider(scrapy.Spider):
    name = "flashscore"
    allowed_domains = ["flashscore.com"]

    def parse(self, response):
        """
        Абстрактный метод. Здесь должна быть логика парсинга:
        - матчей
        - команд
        - лиг
        - событий матчей
        """

        # Пример генерации MatchItem (данные можно заменить на фиктивные)
        match_item = MatchItem(
            home_team="Team A",
            away_team="Team B",
            score="2 - 1",
            league="Example League",
            date="2025-11-05T20:00:00"
        )
        yield match_item

        # Пример генерации события матча
        event_item = MatchEventItem(
            match_id=1,
            minute=15,
            event_type="goal",
            team="Team A",
            player="Player 1",
            assist_player="Player 2"
        )
        yield event_item



