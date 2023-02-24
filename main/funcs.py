
def mptt(node, counter, node_list):
    counter += 1
    node.left = counter
    if node.children:
        for child_node in node.children.all():
            counter = mptt(child_node, counter, node_list)
    counter += 1
    node.right = counter
    node.parent_left = node.parent.left if node.parent else 0
    node.parent_right = node.parent.right if node.parent else 0
    node_list.append(node)
    return counter
