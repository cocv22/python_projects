import pygame
import math
pygame.init() #initializes module

WIDTH, HEIGHT = 920, 700 #For window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #sets up the window
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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
        pygame.draw.circle(win, self.color, (x, y), self.radius)
  
def main():
    run = True
    clock = pygame.time.Clock() #This is to limit the simulation speed to a base number
    
    sun = CelestialBodies(0, 0, 30, (254, 211, 60), 1.98892 * 10**30)
    sun.sun = True
    
    earth = CelestialBodies(-1 * CelestialBodies.AU, 0, 10, (40, 122, 184), 5.9722 * 10**24)
    earth.sun = False
    
    mars = CelestialBodies()
    
    celestial_bodies = [sun, earth]
    
    while run:
        clock.tick(60) #updates loop 60 times per sec
        #WIN.fill(WHITE) #Makes the screen a specific color (white)
        
        for event in pygame.event.get(): #gives a list of all different events that occur
            if event.type == pygame.QUIT:
                run = False
        
        for body in celestial_bodies:
            body.draw(WIN)
        
        pygame.display.update() #Updates changes done and essentially draws them onto the screen
            
    pygame.quit()

main()        