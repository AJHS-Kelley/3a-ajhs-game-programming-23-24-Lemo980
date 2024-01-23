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
import pygame, sys, random
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
    
    pygame.init()































