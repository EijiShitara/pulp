import pulp

prob = pulp.LpProblem('production', sense = pulp.LpMaximize)

#variables.
a = pulp.LpVariable('a', lowBound = 0)
b = pulp.LpVariable('b', lowBound = 0)
c = pulp.LpVariable('c', lowBound = 0)
d = pulp.LpVariable('d', lowBound = 0)

#objective.
prob += 5 * a + 3 * b + 2 * c + 4 * d

#constraints.
prob += 2 * a + 1 * d <= 4
prob += 1 * a + 2 * b <= 8
prob += 1 * b + 1 * c <= 6
prob += 2 * c + 2 * d <= 10

#describe the problem.
print(prob)

#execution.
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print('Status:', pulp.LpStatus[status])

#show results.
print('Result')
print('a:', a.value())
print('b:', b.value())
print('c:', c.value())
print('d:', d.value())
print('g:', prob.objective.value())
