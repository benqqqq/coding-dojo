import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                operand_right = stack.pop()
                operand_left = stack.pop()

                match token:
                    case '+':
                        stack.append(operand_left + operand_right)
                    case '-':
                        stack.append(operand_left - operand_right)
                    case '*':
                        stack.append(operand_left * operand_right)
                    case '/':
                        stack.append(math.trunc(operand_left / operand_right))

                continue

            try:
                int_token = int(token)
            except ValueError:
                raise Exception(f'Unsupported token {token}')
            else:
                stack.append(int_token)

        return stack[0]
