from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r") as file:
        list_job = csv.DictReader(file)
        return list(list_job)


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_type = set([job["job_type"] for job in data])
    print(list(job_type))
    return list(job_type)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_job_type.append(job)
    return list_job_type
