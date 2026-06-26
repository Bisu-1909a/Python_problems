"""gradebook.stats — aggregate statistics over grade records."""

from typing import List, Dict, Set, Tuple

def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    scores = {}   # dictionary: name -> list of scores
    for r in records:
        name = r["name"]
        score = r["score"]
        if name not in scores:
            scores[name] = []   
        scores[name].append(score)

    averages = {}
    for name in scores:
        total = 0
        count = 0
        for s in scores[name]:
            total = total + s
            count = count + 1
        avg = total / count
        averages[name] = round(avg, 2)
    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    subjects = set()
    for r in records:
        subjects.add(r["subject"])
    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    averages = average_per_student(records)
    top_name = None
    top_avg = 0
    for name in averages:
        if averages[name] > top_avg:
            top_name = name
            top_avg = averages[name]
    return (top_name, top_avg)

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    averages = average_per_student(records)
    passing = []
    for name in averages:
        if averages[name] >= threshold:
            passing.append(name)
    passing.sort()   # sort alphabetically
    return passing
