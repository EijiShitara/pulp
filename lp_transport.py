import pulp

prob = pulp.LpProblem('transport')

#variables.
xa = pulp.LpVariable('xa', lowBound = 0)
xb = pulp.LpVariable('xb', lowBound = 0)
xc = pulp.LpVariable('xc', lowBound = 0)
ya = pulp.LpVariable('ya', lowBound = 0)
yb = pulp.LpVariable('yb', lowBound = 0)
yc = pulp.LpVariable('yc', lowBound = 0)

#objective function.
prob += 10 * xa + 6 * xb + 16 * xc + 8 * ya + 8 * yb + 4 * yc

#constraints.
prob += xa + xb + xc == 8
prob += ya + yb + yc == 16
prob += xa + ya == 12
prob += xb + yb == 4
prob += xc + yc == 8

print(prob)

#execution.
status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status", pulp.LpStatus[status])

#showing results.
print("Result:")
print("xa:", xa.value())
print("xb:", xb.value())
print("xc:", xc.value())
print("ya:", ya.value())
print("yb:", yb.value())
print("yc:", yc.value())

print("objective:", prob.objective.value())
