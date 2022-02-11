# Algorithm for approximating pi.
# Generating the series: 1 -1/3+1/5-1/7 ... = pi/4
k = 1
s = 0
for i in range(100000):
    if i % 2 == 0:
        # we multiple by 4 to obtain pi
        s += 4/k
    else:
        # we multiple by 4 to obtain pi
        s -= 4/k
    k += 2
print('Approximation of pi = ', + s)

# For more information see: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80#:~:text=The%20Leibniz%20formula%20for%20%CF%804%20can%20be%20obtained%20by,of%20the%20Dirichlet%20beta%20function
