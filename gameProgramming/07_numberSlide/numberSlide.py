# Number slide game, ELiot Blanton, based on project by Al Sweigart, v0.0

#GAME SETUP/STEPS:
    #layout/setup grid
    #create tiles and add to the board
    #check for valid movements
    #animate tile movement
    #allow for user input to select tile (mouse click)
    #identify location coordinates of mouse click to determine tile selected
    #check for win -- all numbers in order

#Divide and conquer method -- break down the problem into smaller problems, then solve those problems

#board setup data
BOARDWIDTH = 4 #columns
BOARDHIGHT = 4 #rows

#tile size
TILESIZE = 80 #measured in pixels

#Window size
WINDOWWIDTH = 640 #measured in pixels
WINDOWHEIGHT = 480 #measured in pixels

#frames per second
FPS = 30 #sets maximum, does not improve performance on a potato

#blank tile value
BLANK = None


#color values
#min value -- 0           max value -- 255
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

#assign colors to game objects
BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOE = BRIGHTBLUE

#Font size
BASICFONTSIZE = 20 #Measured in pixels



