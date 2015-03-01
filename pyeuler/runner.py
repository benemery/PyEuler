from clint.textui import puts, indent, colored
import multiprocessing

def solve_problems(problems, solutions, timeout=60):
    """Solve a list of problems and update the console with status"""
    puts('Solving %s problems' % len(problems))

    for problem in problems:
        message = str(problem.number)
        output_queue = multiprocessing.Queue()
        p = multiprocessing.Process(target=test_problem, name="Solve", args=(problem, solutions, output_queue))
        p.start()

        p.join(timeout)

        if p.is_alive():
            message += ' ' + colored.yellow('Too slow')
            p.terminate()
            p.join()
        else:
            problem = output_queue.get()
            if problem.correctly_solved:
                message += ' ' + colored.green('OK')
            else:
                message += ' ' + colored.red('FAIL. [Result: %s]' % problem.result)

        with indent(4):
            puts(message)

def test_problem(problem, solutions, output_queue):
    result = problem.solve()
    problem.correctly_solved = result == solutions[str(problem.number)]
    output_queue.put(problem)
