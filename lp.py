import pulp

prob = pulp.LpProblem('lp')

#defining variables.
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

#objective function.
prob += x + y + 1

#constraints.
prob += 3 * x + 5 * y <= 15
prob += 2 * x + y >= 4
prob += x - y == 1

print(prob)

#execution.
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status:", pulp.LpStatus[status])

#print result.
print("Result:")
print("x", x.value())
print("y", y.value())
print("objective", prob.objective.value())
