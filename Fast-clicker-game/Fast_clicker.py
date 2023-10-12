import pygame
import time
pygame.init()
'''creating the program window'''
back = (200, 255, 255) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
clock = pygame.time.Clock()



pygame.display.update()
clock.tick(40)