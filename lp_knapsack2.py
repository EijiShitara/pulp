import pulp

def solver(w):
    # goods
    goods = ['a', 'b', 'c', 'd']
    # price
    price = [91, 120, 610, 930]
    # weight
    weight = [3, 4, 20, 30]

    prob = pulp.LpProblem('knapsack2', sense = pulp.LpMaximize)
    # 
    xs = [pulp.LpVariable('{}'.format(x), cat='Integer', lowBound=0) for x in goods]
    # 目的関数
    prob += pulp.lpDot(price, xs)
    # 制約条件
    prob += pulp.lpDot(weight, xs) <= w

    print(prob)

    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
    print("Status", pulp.LpStatus[status])
    print([x.value() for x in xs])
    print(prob.objective.value())
