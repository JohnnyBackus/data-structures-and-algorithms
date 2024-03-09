from data_structures.binary_tree import BinaryTree, Node as Tree_Node
from data_structures.queue import Queue

### Fixed Queue dequeue method so this function works now. Need to refactor.

def breadth_first(tree):
    staging = Queue()
    node_list = []

    if tree.root == None:
        return []

    staging.enqueue(tree.root)
    # print("tree.root:", tree.root)

    def traverse_tree(node):
        # nonlocal staging
        # print("node.value:", node.value)
        if node.left:
            new_node = node.left
            # print("node.left:", node.left)
            # print("node.left.value:", node.left.value)
            staging.enqueue(new_node)
            # print("staging.peek().value:", staging.peek().value)
        if node.right:
            new_node = node.right
            staging.enqueue(new_node)
        check_staging()


    def check_staging():
        # nonlocal staging
        # nonlocal node_list
        while not staging.is_empty():
            # print("staging.peek().value:", staging.peek().value)
            dequeued_node = staging.dequeue()
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
