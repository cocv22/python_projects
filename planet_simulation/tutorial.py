import pygame
import math
pygame.init() #initializes module

WIDTH, HEIGHT = 800, 800 #For window
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #sets up the window
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)

def main():
    run = True
    clock = pygame.time.Clock() #This is to limit the simulation speed to a base number
    
    while run:
        clock.tick(60) #updates loop 60 times per sec
        #WIN.fill(WHITE) #Makes the screen a specific color (white)
        #pygame.display.update() #Updates changes done and essentially draws them onto the screen
        
        for event in pygame.event.get(): #gives a list of all different events that occur
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()

main()        