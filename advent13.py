import re
import io

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

def min_tokens_to_win(aX, aY, bX, bY, pX, pY):
    memo = {}
    
    def dfs(currX, currY, tokens):
        if (currX, currY) in memo:
            return memo[(currX, currY)]
        
        if currX == pX and currY == pY:
            return tokens
        if currX > pX or currY > pY:
            return float('inf')
        
        # Move by pressing button A
        tokens_a = dfs(currX + aX, currY + aY, tokens + 3)
        # Move by pressing button B
        tokens_b = dfs(currX + bX, currY + bY, tokens + 1)
        
        memo[(currX, currY)] = min(tokens_a, tokens_b)
        return memo[(currX, currY)]
    
    result = dfs(0, 0, 0)
    return result if result != float('inf') else None

total_tokens = 0
for line in lines.split("\n\n"):
    a, b, p = line.split("\n")
    aX, aY = map(int, re.findall("\d+", a))
    bX, bY = map(int, re.findall("\d+", b))
    pX, pY = map(int, re.findall("\d+", p))
    
    result = min_tokens_to_win(aX, aY, bX, bY, pX, pY)
    if result is not None:
        total_tokens += result

print(total_tokens)