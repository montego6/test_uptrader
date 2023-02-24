
def mptt(node, counter, node_list):
    counter += 1
    node.left = counter
    if node.children:
        for child_node in node.children.all():
            counter = mptt(child_node, counter, node_list)
    counter += 1
    node.right = counter
    node_list.append(node)
    return counter