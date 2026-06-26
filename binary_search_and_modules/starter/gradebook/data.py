"""gradebook.data — hardcoded sample grade records.

This module exists so the rest of the package has data to work on without
needing any file I/O. In a real project this might be a database query or
an API call; here it's just a Python list of dicts.
"""

RECORDS: list[dict] = [
    {"name": "Alice",   "subject": "Math",    "score": 88},
    {"name": "Alice",   "subject": "Science", "score": 92},
    {"name": "Alice",   "subject": "English", "score": 79},
    {"name": "Bob",     "subject": "Math",    "score": 72},
    {"name": "Bob",     "subject": "Science", "score": 85},
    {"name": "Bob",     "subject": "English", "score": 90},
    {"name": "Charlie", "subject": "Math",    "score": 95},
    {"name": "Charlie", "subject": "Science", "score": 88},
    {"name": "Charlie", "subject": "English", "score": 91},
    {"name": "Diana",   "subject": "Math",    "score": 60},
    {"name": "Diana",   "subject": "Science", "score": 70},
    {"name": "Diana",   "subject": "English", "score": 65},
    ]
