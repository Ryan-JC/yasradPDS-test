"""
commands.py
The command-line frontend (argparse): run, dispersion, compare, geometry, --version, etc.

Kept thin: parse arguments, load the design, call the core, print.
Results go to stdout, errors and progress go to stderr.
Exit codes:
    - 0: ok
    - 1: analysis/validation error
    - 2: bad arguments
    - 3: file unreadable
"""