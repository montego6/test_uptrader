
def mptt(node, counter):
    counter += 1
    node.left = counter
    if node.children:
        for child_node in node.children.all():
            counter = mptt(child_node, counter)
    counter += 1
    node.right = counter
    return counter