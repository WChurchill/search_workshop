current_node = start_node  # we are given the starting state
history = set()  # keep track of nodes already visited
queue = []  # use python list as queue
while not goal_test(current_node):
    for child in successors(current_node):
        if child not in history:
            queue.append(child)  # add nodes to list
    current_node = queue.popleft()  # go to the next state
