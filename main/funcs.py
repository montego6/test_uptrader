
def mptt(node, counter, node_list, level):
    counter += 1
    node.left = counter
    node_list.append(node)
    for child_node in node.children.all():
        counter = mptt(child_node, counter, node_list, level+1)
    counter += 1
    node.right = counter
    node.level = level
    return counter
