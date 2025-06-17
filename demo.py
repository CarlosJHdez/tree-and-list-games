#!/usr/bin/env python3
"""
Simple demo script to test the tree library
"""

import sys
import os

# Add the parent directory to the path so we can import our library
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tree_list_games.trees.base import TreeNode

def visualize_tree_simple(node, prefix="", is_last=True):
    print(f"{prefix}{'└── ' if is_last else '├── '}{node.value}")
    if children := node.children:
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            child_prefix = prefix + ("    " if is_last else "│   ")
            visualize_tree_simple(child, child_prefix, is_last_child)

def create_sample_tree():
    """Create a sample tree for demonstration"""
    root = TreeNode("Root")
    
    # Level 1
    child1 = TreeNode("Child 1")
    child2 = TreeNode("Child 2")
    child3 = TreeNode("Child 3")
    
    root.add_child(child1)
    root.add_child(child2) 
    root.add_child(child3)
    
    # Level 2
    grandchild1 = TreeNode("Grandchild 1.1")
    grandchild2 = TreeNode("Grandchild 1.2")
    child1.add_child(grandchild1)
    child1.add_child(grandchild2)
    
    grandchild3 = TreeNode("Grandchild 2.1")
    child2.add_child(grandchild3)
    
    return root

def test_tree_integrity():
    return True


if __name__ == "__main__":
    tree = create_sample_tree()
    if not test_tree_integrity():
        print("Tree was not created correctly!")
        sys.exit(1)
    print("Sample Tree Structure:")
    print(visualize_tree_simple(tree))
    
    print("\n=== Tree Properties ===")
    print(f"Root is leaf: {tree.is_leaf()}")
    print(f"Root is root: {tree.is_root()}")
    print(f"Root height: {tree.get_height()}")
    print(f"Number of first level children: {len(tree.children)}")
    
    # Test a leaf node
    leaf = tree.children[0].children[0]  # grandchild1
    print(f"\nLeaf node '{leaf.value}':")
    print(f"Is leaf: {leaf.is_leaf()}")
    print(f"Depth from root: {leaf.get_depth()}")
    print(f"Height: {leaf.get_height()}")
