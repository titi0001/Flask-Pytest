from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_ind = set(
        [ind["industry"].strip() for ind in data if ind["industry"]]
    )
    return list(unique_ind)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_ind = []
    for ind in jobs:
        if ind["industry"] == industry:
            list_ind.append(ind)
    return list_ind
