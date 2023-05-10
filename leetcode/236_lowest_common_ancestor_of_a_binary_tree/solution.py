# Definition for a binary tree node.
import typing



"""
After solution : 

we can use a simpler method to implement : 

1. travel from top to down
2. if found one of p or q, marked the path 
3. if found another one, look back the path, found the one who is marked   
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class EnhancedTreeNode:
    def __init__(self, x) -> None:
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.tree_node = None
        self.visited = False


EnhancedTreeNodeMapping = typing.Dict[TreeNode, EnhancedTreeNode]


def build_enhanced_tree(node: TreeNode, mapping: EnhancedTreeNodeMapping) -> EnhancedTreeNode:
    enhanced_node = EnhancedTreeNode(node.val)
    enhanced_node.tree_node = node
    mapping[node] = enhanced_node

    if node.left:
        enhanced_node.left = build_enhanced_tree(node.left, mapping)
        enhanced_node.left.parent = enhanced_node
    if node.right:
        enhanced_node.right = build_enhanced_tree(node.right, mapping)
        enhanced_node.right.parent = enhanced_node

    return enhanced_node


def marked_path_up_from(node: EnhancedTreeNode) -> None:
    while node:
        node.visited = True
        node = node.parent


def find_marked_path_up(node: EnhancedTreeNode) -> EnhancedTreeNode:
    while node:
        if node.visited:
            return node
        node = node.parent


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # build a new tree with parent information inside each node
        enhanced_tree_mapping: EnhancedTreeNodeMapping = {}
        build_enhanced_tree(root, enhanced_tree_mapping)

        # travel p and mark the path
        marked_path_up_from(enhanced_tree_mapping.get(p))

        # travel q and break if there is on the previous p path
        return find_marked_path_up(enhanced_tree_mapping.get(q)).tree_node
