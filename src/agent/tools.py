"""Расчётные инструменты ИИ-агента."""

import math


def ipr_vogel(
    p_res: float,
    p_test: float,
    q_test: float,
    p_wf: float
) -> float:
    """Расчёт дебита по Фогелю, м³/сут."""

    if p_res <= 0:
        raise ValueError("Пластовое давление должно быть положительным")

    if not (0 <= p_test < p_res):
        raise ValueError("Некорректное тестовое давление")

    if not (0 <= p_wf <= p_res):
        raise ValueError("Некорректное забойное давление")

    if q_test <= 0:
        raise ValueError("Тестовый дебит должен быть положительным")

    test_ratio = p_test / p_res
    target_ratio = p_wf / p_res

    denominator = 1 - 0.2 * test_ratio - 0.8 * test_ratio**2
    numerator = 1 - 0.2 * target_ratio - 0.8 * target_ratio**2

    return q_test * numerator / denominator


def arps_decline(
    q0: float,
    annual_decline: float,
    years: float
) -> float:
    """Экспоненциальное падение дебита, м³/сут."""

    if q0 < 0:
        raise ValueError("Начальный дебит не может быть отрицательным")

    if annual_decline < 0:
        raise ValueError("Коэффициент спада не может быть отрицательным")

    if years < 0:
        raise ValueError("Время не может быть отрицательным")

    return q0 * math.exp(-annual_decline * years)
