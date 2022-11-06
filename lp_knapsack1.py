import pulp

prob = pulp.LpProblem('knapsack1', sense = pulp.LpMaximize)

# goods
goods = ['a', 'b', 'c']
# price
price = [6, 4, 1]
# weight
weight = [4, 3, 1]

# variables
xs = [pulp.LpVariable('{}'.format(x), cat='Integer', lowBound=0) for x in goods]
# objective function
prob += pulp.lpDot(price, xs)
# constraint
prob += pulp.lpDot(weight, xs) <= 10

print(prob)

status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
print("Status", pulp.LpStatus[status])
print([x.value() for x in xs])
print("Price in total:", prob.objective.value())
