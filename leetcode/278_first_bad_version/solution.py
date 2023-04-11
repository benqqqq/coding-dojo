# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n

        # [1, 2, 3, 4, 5]
        # [g, g, b, b, b]
        # [g, g, g, b, b]

        while True:
            # some proper timing to exit
            if not isBadVersion(lower_bound) and isBadVersion(lower_bound + 1):
                return lower_bound + 1

            if isBadVersion(lower_bound):
                # we can assume all the version below lower_bound is good
                return lower_bound

            # after this, assume lower_bound is good

            if not isBadVersion(upper_bound):
                raise Exception('not possible because we assume there is at least one bad version')

            middle_of_index = (lower_bound + upper_bound) // 2

            if isBadVersion(middle_of_index):
                upper_bound = middle_of_index
            else:
                lower_bound = middle_of_index


class SolutionByChatGPT:
    def firstBadVersion(self, n: int) -> int:
        lower_bound = 1
        upper_bound = n

        while lower_bound < upper_bound:
            middle_of_index = (lower_bound + upper_bound) // 2

            if isBadVersion(middle_of_index):
                upper_bound = middle_of_index
            else:
                lower_bound = middle_of_index + 1

        return lower_bound
