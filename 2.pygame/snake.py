import os
import sys
import random
import pygame
pygame.init()
screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((255,255,255))     # Fill the background white color (red,green,blue)
background = background.convert()  # Convert Surface to make blitting faster
# screen.blit(background,(0,0))
def show_cook_book_love(screen):
    txt = "I love the CookBook!"
    f = SysFont("Arial", 12)
    s = f.render(txt, 1, (0,0,0))
    screen.blit(s, (0,0))
show_cook_book_love()