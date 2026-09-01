class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                x1 = stack.pop()
                x2 = stack.pop()

                if ch == "+":
                    stack.append(x2 + x1)
                elif ch == "-":
                    stack.append(x2 - x1)
                elif ch == "*":
                    stack.append(x2 * x1)
                else:
                    stack.append(int(x2 / x1))

        return stack[-1]