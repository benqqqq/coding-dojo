from pprint import pprint
from typing import List, Dict, Set


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_group_idx_map: Dict[str, int] = {}
        group_idx_emails_map: Dict[int, Set[str]] = {}
        group_idx_name_map: Dict[int, str] = {}
        current_group_idx = 0

        for account in accounts:
            # print('')
            # print(f'account : {account} ==============')
            name, *emails = account

            # find whether there is any email in the previous group, and find the group_idx
            group_idxes = [email_to_group_idx_map[email] for email in emails if email in email_to_group_idx_map]
            group_idxes = list(set(group_idxes))  # make it unique

            # no group_idx found, means that this is a new group
            if not group_idxes:
                target_group_idx = current_group_idx
                current_group_idx += 1
                # print(f'use new group_idx = {group_idx}')
            else:
                target_group_idx = group_idxes[0]

            # update all emails into the group
            for email in emails:
                email_to_group_idx_map[email] = target_group_idx
                if target_group_idx not in group_idx_emails_map:
                    group_idx_emails_map[target_group_idx] = set()
                    group_idx_name_map[target_group_idx] = name

                group_idx_emails_map[target_group_idx].add(email)

            # update all other group's email into the same group
            for group_idx in group_idxes[1:]:
                for email in group_idx_emails_map[group_idx]:
                    email_to_group_idx_map[email] = target_group_idx
                    group_idx_emails_map[target_group_idx].add(email)

                del group_idx_name_map[group_idx]
                del group_idx_emails_map[group_idx]

        result = []
        for idx, emails in group_idx_emails_map.items():
            name = group_idx_name_map[idx]
            result.append([name, *sorted(emails)])

        return result


"""
Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

"""

accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

output = [
    ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]


sample_output_1 = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

accounts_2 = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"],
]

pprint(Solution().accountsMerge(accounts))
pprint(Solution().accountsMerge(accounts_2))
