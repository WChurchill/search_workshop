from heapq import heappush, heappop
from graph import goal_test, successors, start_state

current_state = start_state  # we are given the starting state
cost = 0
history = set()  # keep track of nodes already visited
heap = []  #
current_node = (cost, current_state)
heappush(heap, current_node)
while not goal_test(current_node[1]):
    for child in successors(current_state):
        if child not in history:
            heappush(heap, (cost, child))  # add nodes to list
            set.add(child)
    current_node = heappop(heap)  # go to the next state
