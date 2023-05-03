from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = []
    for row in data:
        if row["max_salary"].isdigit():
            max_salary.append(int(row["max_salary"].strip()))
    return max(max_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = []
    for row in data:
        if row["min_salary"].isdigit():
            min_salary.append(int(row["min_salary"].strip()))
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if (
            job.get("min_salary") is None
            or job.get("max_salary") is None
            or min_salary > max_salary
        ):
            raise ValueError
        return min_salary <= int(salary) <= max_salary
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    range_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                range_salary.append(job)
        except ValueError:
            pass
    return range_salary
