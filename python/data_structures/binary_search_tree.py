from data_structures.binary_tree import BinaryTree, Node, TargetError


class BinarySearchTree(BinaryTree):
  # don't need __init__ if not changing anything from super class

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        def traverse(node, new_node):
            if new_node.value < node.value:
                if node.left is None:
                    node.left = new_node
                    return
                else:
                    traverse(node.left, new_node)
            elif new_node.value > node.value:
                if node.right is None:
                    node.right = new_node
                else:
                    traverse(node.right, new_node)

        return traverse(self.root, node)


    def contains(self, value):
        if self.root is None:
            raise TargetError(Exception("Tree is empty"))

        def traverse(node, value):
            if value == node.value:
                return True
            if value < node.value:
                if node.left is None:
                    return False
                else:
                    return traverse(node.left, value)  # Add return statement
            elif value > node.value:
                if node.right is None:
                    return False
                else:
                    return traverse(node.right, value)  # Add return statement

        return traverse(self.root, value)
