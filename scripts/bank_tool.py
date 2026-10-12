#!/usr/bin/env python3
"""Run the companion app CLI without duplicating its validation code."""
import argparse
import os
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description='question-bank-builder shared Lecture2Exam bank tool')
parser.add_argument('--app', type=Path, help='Lecture2Exam checkout (or LECTURE2EXAM_HOME)')
args, remaining = parser.parse_known_args()
if args.app:
    candidates = [args.app]
elif os.environ.get('LECTURE2EXAM_HOME'):
    candidates = [Path(os.environ['LECTURE2EXAM_HOME'])]
else:
    candidates = [parent / 'Lecture2Exam' for parent in Path(__file__).resolve().parents]
root = next((candidate.expanduser().resolve() for candidate in candidates if (candidate.expanduser() / 'bank_cli.py').is_file()), None)
if root is None:
    parser.error('Lecture2Exam was not found. Specify --app /path/to/Lecture2Exam or LECTURE2EXAM_HOME.')
sys.path.insert(0, str(root))
from bank_cli import main
sys.exit(main(remaining))
