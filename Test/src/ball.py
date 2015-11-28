#! /usr/bin/env/Python
#! -*- encoding: utf-8 -*-

import sys, pygame
from pygame.constants import KEYDOWN, K_ESCAPE
pygame.init()

size = width, height = 1080, 720
speed = [1, 1]

black = 0, 0, 255

screen = pygame.display.set_mode(size)
_HAND_CURSOR = (
"     XX         ",
"    X..X        ",
"    X..X        ",
"    X..X        ",
"    X..XXXXX    ",
"    X..X..X.XX  ",
" XX X..X..X.X.X ",
"X..XX.........X ",
"X...X.........X ",
" X.....X.X.X..X ",
"  X....X.X.X..X ",
"  X....X.X.X.X  ",
"   X...X.X.X.X  ",
"    X.......X   ",
"     X....X.X   ",
"     XXXXX XX   ")
_HCURS, _HMASK = pygame.cursors.compile(_HAND_CURSOR, ".", "X",'Y')
HAND_CURSOR = ((16, 16), (5, 1), _HCURS, _HMASK)
pygame.mouse.set_cursor(*HAND_CURSOR)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == KEYDOWN and event.key==K_ESCAPE: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    

    screen.fill(black)#要填充黑色，然后再呈现图形，这样才能形成动画。
    screen.blit(ball, ballrect)#根据球的位置来呈现球，存在buffer里。
    #这是真正使图形可见，如果一开始使用blit/fill
    #就可以将图形可见，那么动画就会一帧一帧的呈现而不是
    #等所有的图形都加载到buffer里然后一起呈现
    pygame.display.flip()
    
