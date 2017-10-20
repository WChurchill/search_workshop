current_node = start_node  # we are given the starting state
history = set()  # keep track of nodes already visited
stack = []  # use python list as stack
while not goal_test(current_node):
    for child in successors(current_node):
        if child not in history:
            queue.append(child)  # concatenate 2 lists
    current_node = stack.pop()  # go to the next state
