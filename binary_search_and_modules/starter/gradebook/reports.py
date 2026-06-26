from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    total_records = 0
    for _ in records:
        total_records = total_records + 1

    subjects = list(subjects_offered(records))
    subjects.sort()

    averages = average_per_student(records)
    top_name, top_avg = top_scorer(records)
    passing = passing_students(records, threshold=60.0)

    lines = []
    lines.append("=== Gradebook Report ===")
    lines.append(f"Total records: {total_records}")   #Add a line of text
    lines.append(f"Subjects offered: {', '.join(subjects)}")  #Add a line listing all subjects
    lines.append("")
    lines.append("Averages:")
    for name in sorted(averages.keys()):
        lines.append(f"  {name:<7}: {averages[name]}")  
    lines.append("")
    lines.append(f"Top scorer: {top_name} ({top_avg})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passing)}")

    return "\n".join(lines)
