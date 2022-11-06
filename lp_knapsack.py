import pulp

prob = pulp.LpProblem('knapsack1', sense = pulp.LpMaximize)

# list of goods.
goods = ['a', 'b', 'c', 'd', 'e']

# list of goods' price.
price = [4, 5, 6, 8, 10]

# list of goods' weight.
weight = [3, 4, 5, 7, 9]

# variables.
xs = [pulp.LpVariable('{}'.format(x), cat='Binary') for x in goods]

# objective function.
prob += pulp.lpDot(price, xs)

# constraint.
prob += pulp.lpDot(weight, xs) <= 15

print(prob)

status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status:", pulp.LpStatus[status])
print([x.value() for x in xs])
print(prob.objective.value())
