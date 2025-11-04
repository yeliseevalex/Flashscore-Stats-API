from typing import List

def average_goals(goals: List[int]) -> float:
    """Вычисляет среднее количество голов"""
    if not goals:
        return 0.0
    return round(sum(goals) / len(goals), 2)
