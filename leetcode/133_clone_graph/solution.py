"""
# Definition for a Node.
"""
from typing import Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned_node_map = {}

        cloned_node = Node(val=node.val, neighbors=[])
        travel_and_clone_node(node=node, cloned_node=cloned_node, cloned_node_map=cloned_node_map)

        return cloned_node


def travel_and_clone_node(node: Node, cloned_node: Node, cloned_node_map: Dict[int, Node]) -> None:
    cloned_node_map[node.val] = cloned_node

    for neighbor in node.neighbors:
        cloned_neighbor = cloned_node_map.get(neighbor.val)

        if cloned_neighbor:
            cloned_node.neighbors.append(cloned_neighbor)
        else:
            cloned_neighbor = Node(val=neighbor.val, neighbors=[])
            cloned_node.neighbors.append(cloned_neighbor)
            travel_and_clone_node(neighbor, cloned_neighbor, cloned_node_map)



"""
deep clone 
create a new node at start

when travel each node, we clone its node and neighbors

- when to stop
- how to traverse
- how to clone 

- dfs , marked visited node


"""
