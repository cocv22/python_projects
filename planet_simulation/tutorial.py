import pygame
import math
pygame.init() #initializes module

WIDTH, HEIGHT = 1080, 920 #For window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #sets up the window
pygame.display.set_caption("Planet Simulation")

FONT = pygame.font.SysFont("newromans", 16)

class CelestialBodies:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250/AU # 1 AU = to about 250 pixels
    TIMESTEP = 3600*24 # 1 day
    
    def __init__(self, x, y, radius, color, mass, temperature = None): #Initializes planet with needed attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        
        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self, win): #Draws planets into the given window
        x = self.x * self.SCALE + WIDTH/2 #Adding the width and the height offsets the postition so that they're the center
        y = self.y * self.SCALE + HEIGHT/2
        
        if len(self.orbit) > 2:  
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                updated_points.append((x, y))
            
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 3)}km", 1, (255, 255, 255)) #How you create a text object you can draw
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_width()/2))
        
        pygame.draw.circle(win, self.color, (x, y), self.radius)
        
    def attraction(self, other):
        other_x, other_y = other.x, other.y #Gets coordinates of the planet and sets it to local vars.
        #We get the distance in between the planets
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(pow(distance_x, 2) + pow(distance_y, 2))
        
        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass * other.mass/distance ** 2
        theta = math.atan2(distance_y, distance_x) #atan2 is a special function that gives us the angle associated to these two distances.
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        
        return force_x, force_y #This returns the force in the x and y direction.

    def update_pos(self, celestial_bods): #updates the position according to the force
        total_fx = 0
        total_fy = 0 
        
        for body in celestial_bods:
            if self == body: #makes sure to avoid zero division
                continue
            
            fx, fy = self.attraction(body)
            total_fx += fx
            total_fy += fy
        
        #We get the velocity in x and y direction by multiplying the timestamp
        self.x_vel += total_fx/self.mass * self.TIMESTEP 
        self.y_vel += total_fy/self.mass * self.TIMESTEP
        
        #We multiply the timestamp again to get displacement and add it to the x and y axis of the current planet
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        
def main():
    run = True
    clock = pygame.time.Clock() #This is to limit the simulation speed to a base number
    
    sun = CelestialBodies(0, 0, 50, (254, 254, 80), 1.98892 * 10**30)
    sun.sun = True
    
    mercury = CelestialBodies(-0.4 * CelestialBodies.AU, 0, 7.7, (229, 229, 229), 3.3011 * 10**23)
    mercury.sun = False
    mercury.y_vel = 47.4 * 1000
    
    venus = CelestialBodies(-0.72 * CelestialBodies.AU, 0, 19, (255, 198, 73), 4.867 * 10**24)
    venus.sun = False
    venus.y_vel = 35.02 * 1000
    
    earth = CelestialBodies(-1 * CelestialBodies.AU, 20, 20, (40, 122, 184), 5.9722 * 10**24)
    earth.sun = False
    earth.y_vel = 29.783 * 1000
    
    mars = CelestialBodies(-1.52 * CelestialBodies.AU, 0, 10.6, (193, 68, 14), 6.417 * 10**23)
    mars.sun = False
    mars.y_vel = 24.077 * 1000
    
    celestial_bodies = [sun, mercury, venus, earth, mars]
    
    while run:
        clock.tick(60) #updates loop 60 times per sec
        WIN.fill((0, 0, 0)) #Makes the screen a specific color (white)
        
        for event in pygame.event.get(): #gives a list of all different events that occur
            if event.type == pygame.QUIT:
                run = False
        
        for body in celestial_bodies:
            body.update_pos(celestial_bodies)
            body.draw(WIN)
        
        pygame.display.update() #Updates changes done and essentially draws them onto the screen
            
    pygame.quit()

main()        