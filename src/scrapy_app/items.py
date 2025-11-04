import scrapy

class MatchItem(scrapy.Item):
    """Информация о матче"""
    home_team = scrapy.Field()
    away_team = scrapy.Field()
    score = scrapy.Field()
    league = scrapy.Field()
    date = scrapy.Field()


class MatchEventItem(scrapy.Item):
    """События матча: голы, карточки, замены"""
    match_id = scrapy.Field()
    minute = scrapy.Field()
    event_type = scrapy.Field()
    team = scrapy.Field()
    player = scrapy.Field()
    assist_player = scrapy.Field()
