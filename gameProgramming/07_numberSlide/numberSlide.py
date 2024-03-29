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

#Module imports -- import whole module
import pygame, sys, random, time
#sys module gives access to system level functions including open/closing programs, etc.

#Module imports -- specific functions
from pygame.locals import *
#this line allows us to call functions diewctly instead of pygame.function()
#we can just write function()
# * in this line is a wildcard and means any or all
# EX: delete myGameFiles*

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

#buttons and messages
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

#window margins
XMARGIN = int ((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1)))/2)
YMARGIN = int ((WINDOWHEIGHT - (TILESIZE * BOARDHIGHT + (BOARDHIGHT -1)))/2)

#Directional assignments
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

#--------------------MAIN GAME LOOP-------------------------+
def main():
    #global keyword makes Python use the same variable in entire program
    global FPSCLOCK, DISPLAYSURF, BASIC_FONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT
    #surf is the general abbreviation for 'surface'
    #a 'surface' in pygame can be used to draw graphics, text, or simple colors
    #The easiest way to think about a surface is a whiteboard

    #Rect is the abbreviation for rectangle

    #start the pygame module itself. this line of code is required for pygame to work
    
    pygame.init()#Start pygame module
    FPSCLOCK = pygame.time.Clock() #establish the start to track FPS
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #creates actual game window
    pygame.display.set_caption('Eliot\'s sliding puzzle game')
    time.sleep(5)


#End the game
def terminate():
    pygame.quit()#this will end all pygame events
    sys.exit()#quits program using OS command

# check if the player quits
def checkForQuit() -> None:
    for event in pygame.event.get(quit):
        terminate()#terminate game if quit event is present
    for event in pygame.event.get(KEYUP): #triggers when the specific key is released
        if event.key == K_ESCAPE: #trigger if escape key is released
            terminate()
        pygame.event.post(event)# put other events at the back of the que.

def getLeftTopOfTile(tileX: int, tileY: int) -> tuple:
    left = XMARGIN =(tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN =(tileY * TILESIZE) + (tileY - 1)
    return (top, left)

def getSpotClick(board: list, x: int, y: int) -> tuple:
    for tileX in range(len(board)): #loop through each tile on the x axis once
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY) #Tell us where the tile is
            tileRect = pygame.rect(left, top, TILESIZE, TILESIZE)
            #pygame.Rect(left, top, width, height)
            if tileRect.collidepoint(x, y): #does out object hit something at (x, y)?
                #.collidepoint is basically battleship
                return (tileX, tileY) #if we hit, return the location
    return(None, None) # if we miss, return None, None.




    return(None, None)



main()






























