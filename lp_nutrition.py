import pulp

prob = pulp.LpProblem('nutrition')

#variables
a = pulp.LpVariable('a', lowBound = 0)
b = pulp.LpVariable('b', lowBound = 0)
c = pulp.LpVariable('c', lowBound = 0)

#objective function.
prob += 4 * a + 2 * b + 5 * c

#constraints.
prob += 3 * a + 1 * b + 2 * c >= 15
prob += 1 * a + 2 * b + 4 * c >= 10

print(prob)

# execution.
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status", pulp.LpStatus[status])

#print result.
print("Result")
print("a:", a.value())
print("b:", b.value())
print("c:", c.value())
print("objective:", prob.objective.value())
