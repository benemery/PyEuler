class Problem(object):
    def __init__(self, number, solution):
        self.number = int(number)

        self.text = ""
        self.solution = solution
        self.test = None
        self.correctly_solved = False
        self.result = None

    def solve(self):
        self.result = self.solution()
        return self.result
