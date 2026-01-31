"""Parse weekly schedule file and count distinct subjects and types.

Expected line formats (examples):
  Понеділок
  Математика (лекція)
  Фізика (лабораторна), Хімія (практична)
  Monday

This script counts:
 - number of distinct subjects (by name)
 - number of lectures
 - number of practicals
 - number of labs
 - number of subjects with unknown type

It tolerates multiple subjects per line separated by commas or semicolons,
and recognizes Ukrainian and English keywords for types.
"""
from typing import Dict, Set
import re
import sys
import os

TYPE_MAP = {
    'лекц': 'lecture', 'лекція': 'lecture', 'лекція.': 'lecture', 'лек': 'lecture', 'lecture': 'lecture', 'lek': 'lecture',
    'прак': 'practical', 'практич': 'practical', 'практична': 'practical', 'practical': 'practical', 'prak': 'practical',
    'лаб': 'lab', 'лаборатор': 'lab', 'лабораторна': 'lab', 'lab': 'lab', 'laboratory': 'lab'
}

DAY_WORDS = [
    # Ukrainian days
    'понеділок', 'вівторок', 'середа', 'четвер', 'п\u2019ятниця', "п'ятниця", 'субота', 'неділя',
    # English
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'
]


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def _detect_type(type_str: str) -> str:
    """Return standardized type key: 'lecture'|'practical'|'lab'|None"""
    if not type_str:
        return None
    ts = _normalize(type_str)
    for key, val in TYPE_MAP.items():
        if key in ts:
            return val
    return None


def parse_schedule(path: str, encoding: str = 'utf-8') -> Dict[str, object]:
    """Parse schedule file and return counts.

    Returns dict with keys: subjects (set of names), lecture, practical, lab, unknown
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    subjects: Set[str] = set()
    counts = {'lecture': 0, 'practical': 0, 'lab': 0, 'unknown': 0}

    with open(path, 'r', encoding=encoding) as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            ln = _normalize(line)

            # skip pure day lines
            if any(day in ln.split() for day in DAY_WORDS):
                # But ensure it's not a subject line that also contains day word inside subject name
                # Heuristic: if line has '(' assume subjects
                if '(' not in line:
                    continue

            # Split by commas or semicolons for multiple entries
            parts = re.split(r'[;,]', line)
            for part in parts:
                item = part.strip()
                if not item:
                    continue
                # Find type in parentheses at end or inside
                m = re.search(r"\(([^)]+)\)", item)
                if m:
                    type_raw = m.group(1)
                    typ = _detect_type(type_raw)
                    # subject name is item without the parentheses content
                    subj = re.sub(r"\([^)]*\)", '', item).strip()
                else:
                    # no parentheses -> unknown type; subject is whole item
                    subj = item
                    typ = None

                subj_norm = _normalize(subj)
                # ignore if subject looks like day
                if subj_norm in DAY_WORDS:
                    continue

                if subj_norm:
                    subjects.add(subj_norm)
                    if typ is None:
                        counts['unknown'] += 1
                    else:
                        counts[typ] += 1

    return {'subjects': subjects, 'lecture': counts['lecture'], 'practical': counts['practical'], 'lab': counts['lab'], 'unknown': counts['unknown']}


def print_report(path: str, report: Dict[str, object]) -> None:
    print(f"File: {path}")
    print(f"Distinct subjects: {len(report['subjects'])}")
    print(f"Lectures: {report['lecture']}")
    print(f"Practicals: {report['practical']}")
    print(f"Labs: {report['lab']}")
    print(f"Unknown-type entries: {report['unknown']}")
    if report['subjects']:
        print('\nSubjects:')
        for s in sorted(report['subjects']):
            print('  -', s)


if __name__ == '__main__':
    path = None
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input('Enter schedule file path: ').strip().strip('"').strip("'")

    try:
        report = parse_schedule(path)
        print_report(path, report)
    except Exception as e:
        print('Error:', e)
        # For debugging print repr
        try:
            print('repr(path):', repr(path))
        except Exception:
            pass
