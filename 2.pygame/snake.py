# import os
# import sys
# import random
# import pygame
# pygame.init()
# size=[700,500]
# screen = pygame.display.set_mode(size) # Set screen size of pygame window
# background = pygame.Surface(screen.get_size())  # Create empty pygame surface
# background.fill((255,255,255))     # Fill the background white color (red,green,blue)
# background = background.convert()  # Convert Surface to make blitting faster
# screen.blit(background,(0,0))
# for event in pygame.event.get():
#     if event.type == pygame.QUIT: 
#         mainloop = False # pygame window closed by user
#     elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_ESCAPE:
#             mainloop = False # user pressed ESC
# milliseconds = clock.tick(FPS) # do not go faster than this framerate

#the next line is only needed for python2.x and not necessary for python3.x
# from __future__ import print_function, division
# import pygame

# # Initialize Pygame.
# pygame.init()
# # Set size of pygame window.
# screen=pygame.display.set_mode((640,480))
# # Create empty pygame surface.
# background = pygame.Surface(screen.get_size())
# # Fill the background white color.
# background.fill((80, 0, 100))
# # Convert Surface object to make blitting faster.
# background = background.convert()
# # Copy background to screen (position (0, 0) is upper left corner).
# screen.blit(background, (0,0))
# # Create Pygame clock object.  
# clock = pygame.time.Clock()

# mainloop = True
# # Desired framerate in frames per second. Try out other values.              
# FPS = 60
# # How many seconds the "game" is played.
# playtime = 0.0

# while mainloop:
#     # Do not go faster than this framerate.
#     milliseconds = clock.tick(FPS) 
#     playtime += milliseconds / 1000.0 
    
#     for event in pygame.event.get():
#         # User presses QUIT-button.
#         if event.type == pygame.QUIT:
#             mainloop = False 
#         elif event.type == pygame.KEYDOWN:
#             # User presses ESCAPE-Key
#             if event.key == pygame.K_ESCAPE:
#                 mainloop = False
                
#     # Print framerate and playtime in titlebar.
#     text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime)
#     pygame.display.set_caption(text)

#     #Update Pygame display.
#     pygame.display.flip()

# # Finish Pygame.  
# pygame.quit()

# # At the very last:
# print("This game was played for {0:.2f} seconds".format(playtime))

# #!/usr/bin/env python

# """
# 002_display_fps_pretty.py

# Display framerate and playtime.
# Works with Python 2.7 and 3.3+.

# URL:     http://thepythongamebook.com/en:part2:pygame:step002
# Author:  yipyip
# License: Do What The Fuck You Want To Public License (WTFPL)
#          See http://sam.zoy.org/wtfpl/
# """

# ####

import pygame


####

class PygView(object):


    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           self.clock.get_fps(), " "*5, self.playtime))

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()