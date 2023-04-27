from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        changes = {}

        # O(n*m) = O(10^4 * 12) = O(10^5)
        for current_amount in range(1, amount + 1):  # O(n) -> O(10^4)
            for coin in coins:  # O(m) -> O(12)
                rest_amount = current_amount - coin

                if rest_amount == 0:
                    changes[current_amount] = 1
                    break

                # no possible changes
                if rest_amount not in changes:
                    continue

                # the fist possible changes
                if current_amount not in changes:
                    changes[current_amount] = changes[rest_amount] + 1
                    continue

                # check if there is fewer changes possibility
                changes[current_amount] = min(changes[current_amount], changes[rest_amount] + 1)

        return changes.get(amount, -1)
