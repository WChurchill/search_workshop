current_node_start = start_node  # we are given the starting state
current_node_end = goal_node  # we are given the goal state
history = set()  # keep track of nodes already visited
queue = []  # use python list as queue for start list
queue_end = []  # use python list as queue for end list
while current_node_start not in history:
    children1 = successors(current_node_start)
    children2 = successors(current_node_end)  # predecessors?
    for i, j in range(children1.len()), range(children2.len()):
        if children1[i] not in history:
            queue.append(children1[i])  # add to start list
        if children2[j] not in history:
            queue_end.insert(0, children2[j])  # add to beginning of end list
    current_node_start = queue.popleft()  # go to the next state
    current_node_end = queue_end.popleft()
queue.extend(queue_end)  # holds final path from start to goal
