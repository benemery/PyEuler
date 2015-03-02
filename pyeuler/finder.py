import imp
import os
import re
import sys

from pyeuler.problem import Problem

file_match_re = re.compile(r'(\d+)\.py$')

def find_problems(top, problems_to_find=None):
    """Find problems to test starting at `top`."""
    # Add the parent directory to our python path so imports work
    parent_dir = os.path.join(top, os.pardir)
    sys.path.append(os.path.abspath(parent_dir))
    sys.path.append(os.path.abspath(top))

    if not problems_to_find:
        problems_to_find = []

    # This list will contain the problem functions to be executed
    problems = []
    for root, _, files in os.walk(top):
        for filename in files:
            match = re.match(file_match_re, filename)
            if match:
                module_name = match.groups()[0]

                file, pathname, description = imp.find_module(module_name, [root,])

                module = imp.load_module(module_name, file, pathname, description)

                problem = Problem(number=module_name, solution=module.main)

                if problems_to_find and problem.number in problems_to_find:
                    problems.append(problem)

    # Sort the problems in their order
    problems.sort(key=lambda problem: problem.number)
    return problems
