question = input("You need to run this as sudo or the keyboard wont work. If you are not sudo quit now")

import sys, pygame
import keyboard
import random
pygame.init()

size = width, height = 800, 600
speedx = [1,0]
speed_x = [-1,0]
blue = 255, 255, 255
import keyboard  # using module keyboard
shipX = 0
shipY = 0
speed = 1

screen = pygame.display.set_mode(size)

ball = pygame.image.load("guy.gif")
ballrect = ball.get_rect()
heart = pygame.image.load("heart.gif")
heartrect = heart.get_rect()



while 1:                                            #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if keyboard.is_pressed('s'):  # if key 'w' is pressed
        ballrect.y = ballrect.y + speed
    if keyboard.is_pressed('w'):  # if key 's' is pressed
        ballrect.y = ballrect.y - speed
    if keyboard.is_pressed('a'):  # if key 'a' is pressed
        ballrect.x = ballrect.x - speed    
    if keyboard.is_pressed('d'):  # if key 'd' is pressed
        ballrect.x = ballrect.x + speed
    #if heartrect.collidedict(None):            #broken code dont use
      #  print("it worked")
       
    #screen draw comands
    screen.fill(blue)
    screen.blit(ball, ballrect,)
    screen.blit(heart, heartrect,)
    pygame.display.flip()
    

   