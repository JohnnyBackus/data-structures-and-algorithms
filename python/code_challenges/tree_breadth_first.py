from data_structures.binary_tree import BinaryTree, Node as Tree_Node
from data_structures.queue import Queue

### Unable to get solution to work with Queue class. Unable to enqueue node.left or node.right. ###
### Solution works with list. Changed enqueue methods to append and dequeue methods to pop(0)###

def breadth_first(tree):
    staging = []
    node_list = []

    if tree.root == None:
        return []

    staging.append(tree.root)
    # print("tree.root:", tree.root)

    def traverse_tree(node):
        # nonlocal staging
        # print("node.value:", node.value)
        if node.left:
            new_node = node.left
            # print("node.left:", node.left)
            # print("node.left.value:", node.left.value)
            staging.append(new_node)
            # print("staging.peek().value:", staging.peek().value)
        if node.right:
            new_node = node.right
            staging.append(new_node)
        check_staging()


    def check_staging():
        # nonlocal staging
        # nonlocal node_list
        while staging:
            # print("staging.peek().value:", staging.peek().value)
            dequeued_node = staging.pop(0)
            node_list.append(dequeued_node.value)
            traverse_tree(dequeued_node)

    check_staging()

    return node_list



if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Tree_Node("apples")
    tree.root.left = Tree_Node("bananas")
    tree.root.right = Tree_Node("cucumbers")
    tree.root.right.right = Tree_Node("dates")

    print(breadth_first(tree))
    # print(tree)
    # print(tree.root)
    # print(tree.root.value)
    # print(tree.root.left)
    # print(tree.root.left.value)

    # print(breadth_first(tree))
