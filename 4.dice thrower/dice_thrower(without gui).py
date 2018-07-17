# dice thrower
import random
import os
import pygame
# pygame.init()
# screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
# background = pygame.Surface(screen.get_size())  # Create empty pygame surface
# background.fill((255,255,255))     # Fill the background white color (red,green,blue)
# background = background.convert()
print("Hi! welcome to dice thrower game")
n=int(input("Enter the number of player want to play the game=>"))
if type(n)==int:
	player=[]
	for i in range(n):
		d=input("enter name=>")
		player.append(d)
else:
	print("you are not entering number of players")
h=1
for coun in range(0,n):
		print ("                    ",h,player[coun],":")
		print ("                      you got=>",random.randint(1,6),"\n")
		h=h+1
                             os.system("pause")
		print("\n")  
    	


 #    
