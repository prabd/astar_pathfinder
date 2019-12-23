import math
import pygame

BLACK = (0, 0, 0) # inaccessible
WHITE = (255, 255, 255) # open
GREEN = (0, 255, 0) # closed
RED = (255, 0, 0) # enqueued
BLUE = (0, 0, 255) # final path
YELLOW = (255, 255, 0) # start/end

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 15
HEIGHT = 15
 
# This sets the margin between each cell
MARGIN = 1

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
    min_ind = 0
    min_f = math.inf
    for i in range(0, len(node_list)):
        if node_list[i].f < min_f:
            min_f = node_list[i].f
            min_ind = i
    return min_ind

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
def find_path(grid, start, end, screen, illustrating):

    # Initialize starting node
    s = Node(None, start)
    s.g = 0.0
    s.h = 0.0
    s.f = 0.0
    
    # Open list
    open_nodes = []
    open_nodes.append(s)
    closed_nodes = []

    # Holds all the directions that we can look in
    # Can change so that diagonal movement is prohibited
    directions = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]
    #directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # While open list is not empty
    while len(open_nodes) != 0:
        # Find node with min f, pop from q, push to closed
        index = find_lowest_f(open_nodes)
        node = open_nodes.pop(index)
        closed_nodes.append(node)
        # Update tile as closed 
        grid[node.location[0]][node.location[1]] = 2
        # Draw node as blue (current)
        if illustrating:
            myRect = pygame.Rect((MARGIN + WIDTH) * node.location[1] + MARGIN,
                                (MARGIN + HEIGHT) * node.location[0] + MARGIN,
                                WIDTH,
                                HEIGHT)
            pygame.display.update(pygame.draw.rect(screen, BLUE, myRect))
        
        # Find successors
        for direc in directions:
            loc = [node.location[0] + direc[0], node.location[1] + direc[1]]
            if not is_accessible(loc[0], loc[1], grid):
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
            if lower_f(open_nodes, s) or lower_f(closed_nodes, s):
                continue

            # Else, remove nodes w/ same loc if they exist, and append current
            try:
                while True:
                    open_nodes.remove(s)
            except ValueError:
                open_nodes.append(s)

            if illustrating:
                # Draw sucessor as open (red)
                myRect2 = pygame.Rect((MARGIN + WIDTH) * s.location[1] + MARGIN,
                                    (MARGIN + HEIGHT) * s.location[0] + MARGIN,
                                    WIDTH,
                                    HEIGHT)
                pygame.display.update(pygame.draw.rect(screen, RED, myRect2))
        # Draw node as closed (green)
        if illustrating:
            pygame.display.update(pygame.draw.rect(screen, GREEN, myRect))
    return []

# Initializes screen as grid with white tiles
def initialize_display(grid, screen):
    # Set title of screen
    pygame.display.set_caption("Pathfinder")
    # Set the screen background
    screen.fill(BLACK)
    # Draw the base grid
    for row in range(0, len(grid)):
        for column in range(0, len(grid[0])):
            pygame.draw.rect(screen,
                             WHITE,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    pygame.display.flip()

# Gets user to place obstacles until enter key is pressed
# Returns true if user exits here, false otherwise
def get_obstacles(grid, screen):
    # Loop until the user clicks enter
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Update tiles according to user input until user presses enter
    while not done:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
                done = True
                return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Loop until mouse up
            e = pygame.event.wait()
            while e.type != pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Update that grid position to 1
                try:
                    grid[row][column] = 1
                    color = BLACK
                    
                    # Update tile
                    myRect = pygame.Rect((MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT)
                    pygame.display.update(pygame.draw.rect(screen, color, myRect))
                except IndexError:
                    print("Out of bounds click")
                e = pygame.event.wait()
    
        # Limit to 60 frames per second
        clock.tick(120)
    return False

# Given a list of coordinates, it will draw the path on the screen
def draw_path(path, screen):
    for xy in path:
        row = xy[0]
        col = xy[1]
        myRect = pygame.Rect((MARGIN + WIDTH) * col + MARGIN,
                             (MARGIN + HEIGHT) * row + MARGIN,
                             WIDTH,
                             HEIGHT)
        pygame.display.update(pygame.draw.rect(screen, BLUE, myRect))

def main():
    # Hardcoded rows/cols, maybe allow user to change (within a range)?
    ROWS = 50
    COLS = 50

    # Initialize g
    g = []
    for i in range(0, ROWS):
        g.append([])
        for j in range(0, COLS):
            g[i].append(0)

    # Initialize pygame
    pygame.init()

    # Create screen
    WINDOW_SIZE = [805, 805]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    
    # Initialize display
    initialize_display(g, screen)

    # Set start/end, and whether to illustrate
    # TODO: Allow user to change the following
    illustrate = True # hardcoded as true, allow user to change in future
    start = [0, 0] # hardcoded
    end = [49, 49] # hardcoded

    # Draw start and end in Yellow
    startRec = pygame.Rect((MARGIN + WIDTH) * start[1] + MARGIN,
                           (MARGIN + HEIGHT) * start[0] + MARGIN,
                           WIDTH,
                           HEIGHT)
    endRec = pygame.Rect((MARGIN + WIDTH) * end[1] + MARGIN,
                         (MARGIN + HEIGHT) * end[0] + MARGIN,
                         WIDTH,
                         HEIGHT)
    pygame.display.update(pygame.draw.rect(screen, YELLOW, startRec))
    pygame.display.update(pygame.draw.rect(screen, YELLOW, endRec))

    # Get obstacles from user
    user_exit = get_obstacles(g, screen)
    if user_exit:
        print("Terminated by user")
        return

    # Make sure that start and end are accessible
    g[start[0]][start[1]] = 0
    g[start[0]][start[1]] = 0
    
    # Run algo
    print("Beginning search...")
    path = find_path(g, start, end, screen, illustrate)
    
    # Show results
    if len(path) == 0:
        print("No path found")
    else:
        print("Found a path")
        print(path)
        draw_path(path, screen)

    # Loop to prevent automatic close after algorithm finishes
    # Closes when x-ed out or enter key is pressed
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True




if __name__ == '__main__':
    main()
    pygame.quit()
