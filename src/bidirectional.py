from Maze import Maze


class SearchNode():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

MAZE_SIZE = 20
maze = Maze(MAZE_SIZE, MAZE_SIZE)
goal_test = maze.getTerminalFunc()
successors = maze.getSuccessorFunc()

goal_node_start = SearchNode((0, 0), None)  # we are given the starting state
goal_node_end = SearchNode((MAZE_SIZE - 1, MAZE_SIZE - 1), None)  # we are given the goal state
history = set()  # keep track of nodes already visited
queue = []  # use python list as queue for start list
queue_end = []  # use python list as queue for end list

queue.append(goal_node_start) 
queue_end.append(goal_node_end)  
start_terminated = False

while len(queue) > 0 and len(queue_end) > 0:
    if len(queue) > 0:
        current_node_start = queue.pop(0)

        # Terminate when either one gole node is reached, or the current node
        # has already be traversed by the other tree
        if current_node_start.state == goal_node_end.state or \
        len([x for x in queue_end if x.state == current_node_start.state]) > 0:
            start_terminated = True
            break

        history.add(current_node_start.state)

        for new_state in successors(current_node_start.state):
            if new_state not in history:
                queue.append(SearchNode(new_state,
                                        current_node_start))

    if len(queue_end) > 0:
        current_node_end = queue_end.pop(0)    

        # Terminate when either one gole node is reached, or the current node
        # has already be traversed by the other tree
        if current_node_end.state == goal_node_start.state or \
        len([x for x in queue if x.state == current_node_end.state]) > 0:
            break        

        history.add(current_node_end.state)

        for new_state in successors(current_node_end.state):
            if new_state not in history:
                queue_end.append(SearchNode(new_state,
                                            current_node_end))


# Connect search trees and build path
if start_terminated:
    current_node = current_node_start
else:
    current_node = [x for x in queue if x.state == current_node_end.state][0]

path = set(current_node.state)

while current_node.parent:
    current_node = current_node.parent
    print(current_node.state)
    path.add(current_node.state)

if not start_terminated:
    current_node = current_node_end
else:
    current_node = [x for x in queue_end if x.state == current_node_start.state][0]

path.add(current_node.state)

while current_node.parent:
    current_node = current_node.parent
    path.add(current_node.state)
    
maze.print(path=path)
