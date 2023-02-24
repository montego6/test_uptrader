
def mptt(node, counter, node_list, parent_left, level, stack):
    counter += 1
    node.left = counter
    node_list.append(node)
    if node.children:
        for child_node in node.children.all():
            counter = mptt(child_node, counter, node_list, node.left, level+1, stack)
            stack.append(child_node)
    counter += 1
    node.right = counter
    node.parent_left = parent_left
    node.level = level
    if stack:
        while stack and node.level < stack[-1].level:
            child_node = stack.pop()
            child_node.parent_right = node.right
    return counter
