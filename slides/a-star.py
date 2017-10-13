from heapq import heappush, heappop
from graph import goal_test, successors, start_node, heuristic, cost

current_node = start_node  # we are given the starting state
history = set()  # keep track of nodes already visited
queue = []  # priority queue
while not goal_test(current_node):
    for child in successors(current_node):
        if child not in history:
            h = heuristic(child)
            g = cost(current_node)
            f = g + h
            heappush(queue, (f, child))  # add nodes to list
    current_node = heappop(queue)  # go to the next state
