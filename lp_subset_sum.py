import pulp

#list of prime numbers up to 100.
nums_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97]

#list of the first 20 Fibonacci numbers.
nums_fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
            89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

def solver(seq, n):
    """ seq is a list of integers. n is an integer.
Returns 'Optimal' and a subset of seq if the sum of the subset equals n.
Otherwise returns 'Infeasible.'"""
    prob = pulp.LpProblem('subset_sum')

    #variables.
    var = [pulp.LpVariable('x{}'.format(x), cat='Binary') for x in range(len(seq))]

    #constraint.
    prob += pulp.lpDot(seq, var) == n

    print(prob)

    status = prob.solve(pulp.PULP_CBC_CMD(msg=0))
    print("Status:", pulp.LpStatus[status])
    if status == 1:
        print([seq[i] for i in range(len(seq)) if var[i].value() == 1])
