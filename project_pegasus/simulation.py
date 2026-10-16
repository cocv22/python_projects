import math

def move_robot(position, heading, distance, actual_distance):
    if len(position) != 2:
        raise ValueError("Position must be in format x, y")
    
    start_x, start_y = position
    if not isinstance(start_x, (int, float)) or not isinstance(start_y, (int, float)):
        raise TypeError("Coordinate values must be an int or a float.")
            
    actual_x = start_x + (actual_distance * math.cos(heading))
    actual_y = start_y + (actual_distance * math.sin(heading))
    
    ideal_x = start_x + (distance * math.cos(heading))
    ideal_y = start_y + (distance * math.sin(heading))
    
    err_x = actual_x - ideal_x
    err_y = actual_y - ideal_y
    error = (err_x, err_y)
    
    return (actual_x, actual_y), error

position = (2, 3)
position, error = move_robot(position, 0, 4, 3.8)
print(round(position[0], 2), round(position[1], 2))
position, error = move_robot(position, math.pi/2, 2, 2.2)
print(round(position[0], 2), round(position[1], 2))
position, error = move_robot(position, 0, 3, 2.5)
print(round(position[0], 2), round(position[1], 2))
