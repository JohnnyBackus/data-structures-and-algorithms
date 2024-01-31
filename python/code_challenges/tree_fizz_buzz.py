from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    new_tree = tree.clone()

    def traverse(node):
        if node.value%15 == 0:
            node.value = "FizzBuzz"
        elif node.value%5 == 0:
            node.value = "Buzz"
        elif node.value%3 == 0:
            node.value = "Fizz"
        else:
            node.value = str(node.value)
        if node.children:
            for child in node.children:
                traverse(child)

    traverse(new_tree.root)

    return new_tree
