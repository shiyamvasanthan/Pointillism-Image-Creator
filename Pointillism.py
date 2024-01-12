#Shiyam Vasanthan 
import pygame
import random
import sys

#Get the file name of the source image from the command line arguement and save the image in a variable
img = pygame.image.load(sys.argv[1])

#Get the dimensions of the source image
(source_width, source_height) = img.get_size()

#Create window and scale the window by factor of 2
win = pygame.display.set_mode((source_width * 4, source_height * 4))

#Define color variables for red, green, and blue
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#For each row of the source image
for y in range(source_height):
	#For each column of the source image
	for x in range(source_width):
		#Get the rgb colour value of each pixel of the source image
		(r, g, b, _) = img.get_at((x, y))
		
		#Floor divide the rgb values by 50 to get the number of red, green, and blue pixels to draw for the new image
		r //= 50
		g //= 50
		b //= 50
		
		#Randomly draw the red circles for the new image
		for red_count in range(r):
			pygame.draw.circle(win, red, (x * 4 + random.randint(0, 3), y * 4 + random.randint(0, 3)), 1)
			
		#Randomly draw the green circles for the new image
		for green_count in range(g): 
			pygame.draw.circle(win, green, (x * 4 + random.randint(0, 3), y * 4 + random.randint(0, 3)), 1)
			
		#Randomly draw the blue circles for the new image
		for blue_count in range(b):
			pygame.draw.circle(win, blue, (x * 4 + random.randint(0, 3), y * 4 + random.randint(0, 3)), 1)
	
#Display the new image to the screen for 5 seconds	
pygame.display.update()
pygame.time.delay(5000)

