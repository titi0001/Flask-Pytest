from src.pre_built.counter import count_ocurrences


def test_counter():
    """Verifica se a função count_ocurrences esta retonando a quantidade
    correta de palavaras"""
    assert count_ocurrences("data/jobs.csv", "python") == 1639
    assert count_ocurrences('data/jobs.csv', 'code') == 753
