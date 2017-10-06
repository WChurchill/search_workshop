from heapq import heappush, heappop
from graph import goal_test, successors, start_node

current_node = start_node  # we are given the starting state
history = set()  # keep track of nodes already visited
queue = []  #
while not goal_test(current_node):
    for child in successors(current_node):
        if child not in history:
            heappush(queue, child)  # add nodes to list
    current_node = heappop(queue)  # go to the next state
