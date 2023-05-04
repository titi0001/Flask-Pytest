from src.pre_built.sorting import sort_by
import pytest


@pytest.fixture
def data():
    return [
        {"date_posted": "2000-01-10", "max_salary": 3000, "min_salary": 1000},
        {"date_posted": "2000-01-11", "max_salary": 4000, "min_salary": 2000},
        {"date_posted": "2000-01-12", "max_salary": 5000, "min_salary": 3000}
    ]


def test_sort_by_criteria(data):
    sort_by(data, "min_salary")
    assert data[1]["min_salary"] == 2000

    sort_by(data, "max_salary")
    assert data[0]["max_salary"] == 5000

    sort_by(data, "date_posted")
    assert data[0]["date_posted"] == "2000-01-12"

    with pytest.raises(ValueError):
        sort_by(data, "invalid_criteria")

  
