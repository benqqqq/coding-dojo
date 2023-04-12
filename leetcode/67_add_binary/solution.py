from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_revered = list(reversed(a))
        b_revered = list(reversed(b))
        adding = 0
        added_sum = ''

        for i in range(len(a_revered)):
            if i == len(b_revered):
                break

            a_char = a_revered[i]
            b_char = b_revered[i]

            sum_char, adding = Solution.add(int(a_char), int(b_char), adding)
            added_sum += sum_char

        long_a_or_b = a_revered if len(a_revered) >= len(b_revered) else b_revered
        short_a_or_b = a_revered if len(a_revered) < len(b_revered) else b_revered
        # a len is 3, b len is 5, start from 3,

        for i in range(len(short_a_or_b), len(long_a_or_b)):
            long_a_or_b_char = long_a_or_b[i]
            sum_char, adding = Solution.add(int(long_a_or_b_char), adding)
            added_sum += sum_char

        if adding:
            added_sum += '1'

        return ''.join(reversed(added_sum))

    def add(*nums: int) -> Tuple[str, int]:
        sum_int = sum(nums)
        if sum_int == 0:
            return '0', 0
        elif sum_int == 1:
            return '1', 0
        elif sum_int == 2:
            return '0', 1
        elif sum_int == 3:
            return '1', 1
        else:
            raise Exception('unsupported case of nums')


class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        # make 'a' be longer than 'b', things will be simpler
        if len(b) > len(a):
            tmp = a
            a = b
            b = tmp

        # make 'b' as long as 'a', things will be simpler
        for i in range(len(b), len(a)):
            b = '0' + b

        result = ''
        carry = 0

        # e.g. a_len = 3, for i in range(2, -1, -1) will produce 2, 1, 0
        for i in range(len(a) - 1, -1, -1):
            temp_sum = int(a[i]) + int(b[i]) + carry
            if temp_sum == 0:
                result = '0' + result
                carry = 0
            elif temp_sum == 1:
                result = '1' + result
                carry = 0
            elif temp_sum == 2:
                result = '0' + result
                carry = 1
            elif temp_sum == 3:
                result = '1' + result
                carry = 1
            else:
                raise Exception('Incorrect binary format of inputs')

        if carry:
            result = '1' + result

        return result
