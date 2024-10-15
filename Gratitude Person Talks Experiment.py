w = 1  # Wall
e = 0  # Empty
x = "start"
y = "end"
mapRow = 0
mapRowElement = 0
map = [[w,w,w,w,w,w],
        [e,e,e,e,e,w],
        [e,w,e,w,e,w],
        [e,w,e,w,e,w],
        [e,e,e,w,e,w],
        [w,w,e,w,y,w],
        [x,e,e,w,w,w]]

# Function to find the start position
def findStart(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == x:
                return i, j  # Return row and column of the start
    return None

# Function to perform the search
def search(map, start):
    frontier = [start]  # List of positions to explore
    explored = []  # List of positions already explored

    while frontier:
        current = frontier.pop(0)  # Get the first position from the frontier
        explored.append(current)  # Mark it as explored
        
        # Get current position
        row, col = current
        
        # Check if we reached the end
        if map[row][col] == y:
            return True  # Found the end
        
        # Define the possible moves (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            
            # Check if new position is within bounds and is empty (e)
            if (0 <= new_row < len(map) and
                0 <= new_col < len(map[0]) and
                map[new_row][new_col] == e and
                (new_row, new_col) not in explored and
                (new_row, new_col) not in frontier):
                
                frontier.append((new_row, new_col))  # Add the new position to the frontier
                print(frontier,explored)

    return False  # If we exhaust the frontier without finding the end

# Find the start position
start_position = findStart(map)

# Perform the search
if start_position:
    found = search(map, start_position)
    print("Path to end found:", found)
else:
    print("Start position not found.")
