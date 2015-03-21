"""Py.Euler. A command line tool to help you Project Euler fun!

Usage:
    py.euler [PATH] [--timeout=TIMEOUT] [--problem=PROBLEM]
    py.euler (-h | --help)
    py.euler --version

Arguments:
    PATH        Path to begin searching from.

Options:
    -h --help               Show this screen.
    --version               Show version.
    --timeout=TIMEOUT       How long to give each solution. Project Euler
                            specifies that no problem should take longer
                            than 60s [default: 60].
    --problem=PROBLEM       The problem number check
"""

VERSION = "0.0.1"

__all__ = ['main', ]

import json
import os

BASE_DIR = os.path.dirname(__file__)

if __name__ == 'main':
    # User has executed this as a script, go directly to main
    main()

def main():
    from docopt import docopt
    from pyeuler.finder import find_problems
    from pyeuler.runner import solve_problems

    args = docopt(__doc__, version=VERSION)

    root = args['PATH']
    timeout = int(args["--timeout"])
    problems_to_find = []
    if args['--problem']:
        problems_to_find.append(int(args['--problem']))
    problems = find_problems(root, problems_to_find=problems_to_find)

    with open(os.path.join(BASE_DIR, 'solutions.txt'), 'rb') as fin:
        solutions = json.loads(fin.read())

    solve_problems(problems, solutions=solutions, timeout=timeout)
