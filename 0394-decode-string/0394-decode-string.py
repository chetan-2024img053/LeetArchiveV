class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # Extract string inside brackets
                curr = []
                while stack[-1] != '[':
                    curr.append(stack.pop())

                curr.reverse()
                stack.pop()  # remove '['

                # Extract number
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                num.reverse()
                repeat = int("".join(num))

                # Repeat the string
                decoded = "".join(curr) * repeat

                # Push back to stack
                for c in decoded:
                    stack.append(c)

        return "".join(stack)