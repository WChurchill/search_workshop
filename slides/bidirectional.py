current_node_start = start_node  # we are given the starting state
current_node_end = goal_node # we are given the goal state
history = set()  # keep track of nodes already visited
queue = []  # use python list as queue for start list
queue_end = []  # use python list us queue for end list
while current_node_start not in history:
    for child in successors(current_node_start):
        if child not in history:
            queue.append(child)  # add nodes to start list
	for child2 in successors(current_node_end):
	    if child2 not in history:
		queue_end.insert(0,child2)  # add to beginning of end list
    current_node_start = queue.popleft()  # go to the next state
    current_node_end = queue.popleft()
queue.extend(queue_end)  # holds final path from start to goal
