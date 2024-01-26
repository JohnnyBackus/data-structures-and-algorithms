class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return own_value + left_value + right_value

        return traverse(self.root)

    def in_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return left_value + own_value + right_value

        return traverse(self.root)

    def post_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return left_value + right_value + own_value

        return traverse(self.root)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TargetError(BaseException):
    pass
