import re
import io
import numpy as np

with open("advent13.txt", "r") as f:
    lines = f.read()
    
# Example input
ex = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# lines = io.StringIO(ex)
# lines = lines.read()

res = 0
for line in lines.split("\n\n"):
    a, b, p = line.split("\n")
    aX, aY = map(int, re.findall("\d+", a))
    bX, bY = map(int, re.findall("\d+", b))
    pX, pY = map(int, re.findall("\d+", p))
    pX+=10000000000000
    pY+=10000000000000
    """Part One"""
    # best = 5000
    # for i in range(101):
    #     for j in range(101):
    #         pa = aX * i + bX * j
    #         pb = aY * i + bY * j
    #         if pa == pX and pb == pY:
    #             best = min(best, 3*i + j)
    # if best < 5000:
    #     res += best

    """Part Two"""
    A = np.array([[aX, aY], [bX, bY]])
    A_T = A.T
    R = np.linalg.solve(A_T, [pX, pY])
    # print(np.allclose(np.dot(A_T, R), [pX,pY]))
    print(R)
    pressa = round(R[0])
    pressb = round(R[1])
    if pressa * aX + pressb * bX == pX and pressa * aY + pressb * bY == pY:
        res += 3* pressa + pressb
    # print(A)
    # print(A_T)

print(res)

    
