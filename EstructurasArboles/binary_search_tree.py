from EstructurasArboles.node import Node
from typing import  TypeVar
T = TypeVar("T")
class BinarySearchTree:
    def __init__(self):
        self.root: Node[T] | None = None
        
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def search(self, root,data):
        if root is None or root.val == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.val:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.data = temp.val
            root.data = self.delete(root.right, temp.data)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.data)
            result += self.inorder_traversal(root.right)
        return result
