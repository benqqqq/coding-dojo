from collections import defaultdict
from typing import List, Dict, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prerequisites_map: Dict[int, List[int]] = defaultdict(list)

        for course, prerequisite in prerequisites:
            course_prerequisites_map[course].append(prerequisite)

        visiting = set()
        visited = set()

        for course in course_prerequisites_map.keys():
            if has_cycle(course, course_prerequisites_map, visiting, visited):
                return False

        return True


def has_cycle(
    course: int, course_prerequisites_map: Dict[int, List[int]], visiting: Set[int], visited: Set[int]
) -> bool:
    if course in visited:
        return False
    if course in visiting:
        return True

    visiting.add(course)
    for prerequisite in course_prerequisites_map.get(course, []):
        if has_cycle(prerequisite, course_prerequisites_map, visiting, visited):
            return True

    visited.add(course)
    visiting.remove(course)

    return False
