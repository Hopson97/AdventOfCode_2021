from time import sleep


class Stack:
    param: int = 0
    curly: int = 0
    square: int = 0
    angle: int = 0


score = 0
incompletescores = []
with open("day10/input.txt") as f:

    for line in f:
        stack = []

        for c in line.strip():
            if c in ["(", "<", "[", "{"]:
                stack.append(c)
            elif c == ")":
                if stack.pop() != "(":
                    score += 3
                    break
            elif c == ">":
                if stack.pop() != "<":
                    score += 25137
                    break
            elif c == "]":
                if stack.pop() != "[":
                    score += 57
                    break
            elif c == "}":
                if stack.pop() != "{":
                    score += 1197
                    break
        else:
            incompletescore = 0
            stack.reverse()
            for c in stack:
                if c == "(":
                    incompletescore *= 5
                    incompletescore += 1
                    print(")", end="")
                elif c == "<":
                    incompletescore *= 5
                    incompletescore += 4
                    print(">", end="")
                elif c == "[":
                    incompletescore *= 5
                    incompletescore += 2
                    print("]", end="")
                elif c == "{":
                    incompletescore *= 5
                    incompletescore += 3
                    print("}", end="")
            print()

            incompletescores.append(incompletescore)


print(score)

incompletescores.sort()
print(incompletescores[len(incompletescores) // 2])
