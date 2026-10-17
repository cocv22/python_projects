import math

def move_robot(position, heading, distance, actual_distance, sensor_distance):
    if len(position) != 2:
        raise ValueError("Position must be in format x, y")
    
    start_x, start_y = position
    if not isinstance(start_x, (int, float)) or not isinstance(start_y, (int, float)):
        raise TypeError("Coordinate values must be an int or a float.")
            
    actual_x = start_x + (actual_distance * math.cos(heading))
    actual_y = start_y + (actual_distance * math.sin(heading))
    
    ideal_x = start_x + (distance * math.cos(heading))
    ideal_y = start_y + (distance * math.sin(heading))
    
    estimate_x = start_x + (sensor_distance * math.cos(heading))
    estimate_y = start_y + (sensor_distance * math.sin(heading))
    
    err_x = actual_x - ideal_x
    err_y = actual_y - ideal_y
    
    s_err_x = estimate_x - actual_x
    s_err_y = estimate_y - actual_y
        
    error = (err_x, err_y)
    s_error = (s_err_x, s_err_y)
    
    return ((actual_x, actual_y), (estimate_x, estimate_y)), (error, s_error)

position = (2, 3)
position, error = move_robot(position, 0, 4, 3.8, 3.9)
actual_pos, estimate_pos = position 

print(round(actual_pos[0], 2), round(actual_pos[1], 2), error)
