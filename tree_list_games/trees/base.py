"""
Base tree experiment
"""
from typing import List, Any, Optional
from abc import ABC, abstractmethod

class TreeNode:
    """Generic tree node"""
    
    def __init__(self, value: Any, node_id: Optional[str] = None):
        self.id = node_id or str(id(self))
        self.value = value
        self.parent: Optional['TreeNode'] = None
        self.children: List['TreeNode'] = []
        self.metadata: dict = {}
        
    def add_child(self, child: 'TreeNode') -> None:
        """Add a child node"""
        child.parent = self
        self.children.append(child)
        
    def remove_child(self, child: 'TreeNode') -> bool:
        """Remove a child node"""
        if child in self.children:
            child.parent = None
            self.children.remove(child)
            return True
        return False
        
    def is_leaf(self) -> bool:
        """Check if this is a leaf node"""
        return len(self.children) == 0
        
    def is_root(self) -> bool:
        """Check if this is a root node (no parent)"""
        return self.parent is None
        
    def get_depth(self) -> int:
        """Get the depth of this node from the root"""
        depth = 0
        current = self.parent
        while current:
            depth += 1
            current = current.parent
        return depth
        
    def get_height(self) -> int:
        """Get the height of the subtree rooted at this node"""
        if self.is_leaf():
            return 0
        return 1 + max(child.get_height() for child in self.children)
        
    def __str__(self) -> str:
        return f"TreeNode(id={self.id}, value={self.value})"
        
    def __repr__(self) -> str:
        return self.__str__()

