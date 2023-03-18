import pygame
from Utils import *
from Player import Player
from Brain import Brain
from Population import Population
from Node import Node
import time


# initializing imported module
pygame.init()
print("\n")


population = Population()
p1 = Player()



def main():
    t = 0
    running = True
    while running:
        # Sets window at 60 FPS
        clock.tick(FPS)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Mouse click event
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_f:
                    p1.draw_raycast = not p1.draw_raycast



        # Calculations before drawing
        keys = pygame.key.get_pressed()
        keyPresses(keys, p1)


        fillScreen()
        surface.blit(road_image, road_rect)
        drawWalls()
        displayFPS()

        # p1.calcSpeed()
        # p1.rotatePoints()
        # p1.calcRaycast()
        # p1.draw()

        population.updatePlayersMovement()
        population.checkIfPlayersDied()
        population.updateAllPlayersBrain()
        population.calculateBrainOutput()
        population.calculateBestScore()



        # Updates the screen
        pygame.display.flip()


if __name__ == '__main__':
    main()

