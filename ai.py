from simpleai.search import CspProblem, backtrack

class Solver:
    def __init__(self, factors, operator, solution):
        self.factors = factors
        self.operator = operator
        self.solution = solution

        self.variables = set(solution + ''.join(factors))
        self.variablesTuple = tuple(self.variables)

        self.first_letter_set = set([factor[0] for factor in factors])

        self.first_letter_set.add(solution[0])

        self.domains = {letter:(list(range(1, 10)) if letter in self.first_letter_set else list(range(10))) for letter in self.variables}

    def constraint_unique(self, variables, values):
        return len(values) == len(set(values))

    def constraint_operate(self, variables, values):
        factorList = []
        for factor in self.factors:
            factorString = ''.join(str(values[self.variablesTuple.index(letter)]) for letter in factor)
            factorList.append(int(factorString))

        resultString = ''.join(str(values[self.variablesTuple.index(letter)]) for letter in self.solution)

        if (self.operator == '+'):
            return sum(factorList) == int(resultString)
        elif (self.operator == '*'):
            end = 1
            for factor in factorList:
                end *= factor
            return end == int(resultString)
        else:
            end = factorList[0]
            for factor in factorList[1:]:
                if(self.operator == '-'):
                    end -= factor
                elif(self.operator == '/'):
                    end /= factor
            return end == int(resultString)
        
    def solve(self):
        constraints = [
            (self.variables, self.constraint_unique),
            (self.variables, self.constraint_operate),
        ]

        problem = CspProblem(self.variables, self.domains, constraints)

        return backtrack(problem)