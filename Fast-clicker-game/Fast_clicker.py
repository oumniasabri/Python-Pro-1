import pygame
import time
pygame.init()
'''creating the program window'''
back = (200, 255, 255) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
clock = pygame.time.Clock()

'''Rectangle class'''
class Area():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height) 
      self.fill_color = color


pygame.display.update()
clock.tick(40)