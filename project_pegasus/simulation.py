import math

def move_robot(*position, heading, distance):
    if len(position) != 2:
        raise ValueError("Position must be in format x, y")
    
    x, y = position
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Coordinate values must me an int or a float.")
            
    x += distance * math.cos(heading)
    y += distance * math.sin(heading)
    
    print(round(x, 2), round(y, 2))
    return x, y

print(move_robot(1, "", heading=math.pi, distance=5))