import math

# This class stores info about a location on the grid
class Node():

    # Ctor
    def __init__(self, parent, location):
        self.parent = parent
        self.location = location
        
        self.f = math.inf
        self.g = math.inf
        self.h = math.inf
    
    # for easy comparison
    def __eq__(self, other):
        return self.location[0] == other.location[0] and self.location[1] == other.location[1]

# Helper
# Returns whether a location is valid
def is_accessible(row, col, grid):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    if grid[row][col] == 1 or grid[row][col] == 2:
        return False
    return True

# Helper
# Returns index in list with lowest f
def find_lowest_f(node_list):
    min = 0
    min_f = math.inf
    for i in range(0, len(node_list)):
        if node_list[i].f < min_f:
            min_f = node_list[i].f
            min = i
    return min

# Helper
# Returns true if there exists lower f for same location as node
def lower_f(node_list, node):
    for n in node_list:
        if(n == node):
            if n.f < node.f:
                return True
    return False

# Helper
# Returns Manhattan distance between two location arrays
def m_distance(first, second):
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

# grid is 2-d array of 0s and 1s, where 0s are accessible locations.
# start and end are lists of x y coordinates
# Returns path in array form
def find_path(grid, start, end):

    # Initialize starting node
    s = Node(None, start)
    s.g = 0.0
    s.h = 0.0
    s.f = 0.0
    
    # Possibly use priority queue? However priority may change, so using list
    open = []
    open.append(s)

    # Holds all the directions that we can look in
    directions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]

    # While open list is not empty
    while len(open) != 0:
        # Find node with min f, pop from q, push to closed
        index = find_lowest_f(open)
        node = open.pop(index)
        grid[node.location[0]][node.location[1]] = 2

        # Find successors
        for dir in directions:
            loc = [node.location[0] + dir[0], node.location[1] + dir[1]]
            if not is_accessible(loc[0],loc[1], grid): 
                continue

            s = Node(node, loc)
            # If successor is destination, end search
            if loc[0] == end[0] and loc[1] == end[1]:
                path = []
                path.append(s.location)
                
                while s.parent is not None:
                    s = s.parent
                    path.append(s.location)

                path.reverse()
                return path
            
            # Set f,g,h values
            s.g = node.g + m_distance(node.location, loc)
            s.h = m_distance(loc, end)
            s.f = s.g + s.h

            # if node with same location is in open with lower f,
            # then skip
            if lower_f(open, s):
                continue
            
            # Else, Add node to open list
            open.append(s)
    
    return []


def main():
    g = [[0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0]]
    
    start = [0,0]
    end = [0, 2]
    path = find_path(g, start, end)
    print(path)


if __name__ == '__main__':
    main()
