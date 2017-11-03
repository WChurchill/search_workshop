from Maze import Maze
import time

# Visualize path generation
slow_viz = True


class SearchNode():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

maze = Maze(20, 20)
goal_test = maze.getTerminalFunc()
successors = maze.getSuccessorFunc()
start_node = SearchNode((0, 0), None)

current_node = start_node  # we are given the starting state
history = set()  # keep track of nodes already visited
stack = []  # use python list as stack
while not goal_test(current_node.state):
    history.add(current_node.state)
    for new_state in successors(current_node.state):
        if new_state not in history:
            stack.append(SearchNode(new_state,
                                    current_node))  # concatenate 2 lists
    current_node = stack.pop()  # go to the next state

path = set(current_node.state)
while current_node.parent:
    current_node = current_node.parent
    path.add(current_node.state)

    maze.print(path=path)
    if slow_viz:
        time.sleep(.1)
