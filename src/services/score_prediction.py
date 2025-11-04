from src.services.utils import average_goals
from src.models.match import Match


def weighted_average(values: list[float], weights: list[float]) -> float:
    """Взвешенное среднее"""
    if not values or not weights or len(values) != len(weights):
        return average_goals(values)
    return round(sum(v * w for v, w in zip(values, weights)) / sum(weights), 2)

def calculate_expected_goals(team_matches: list[Match], head_to_head: list[Match] = None, team_id: int = None):
    """
    Рассчитывает ожидаемое количество голов команды
    team_matches: последние N матчей команды
    head_to_head: последние встречи между командами
    team_id: id команды, для правильного подсчета голов
    """
    pass
