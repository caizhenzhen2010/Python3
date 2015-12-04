#! /usr/bin/env/python
#! -*- encoding: utf-8 -*-

import os,sys,pygame
from pygame.locals import *
import objects,config
import logging,time
from pygame.constants import KEYDOWN, K_ESCAPE


"这个模块包含Squish游戏的主要逻辑"


class State:
    """
    泛型游戏状态类，可以处理时间并在给定的表面上显示自身
    """
    def handle(self,event):
        """
        只处理推出时间的默认事件处理
        """
        if event.type==QUIT:
            sys.exit()
        if event.type==KEYDOWN and event.key==K_ESCAPE:
            sys.exit()
    
    def firstDisplay(self,screen):
        """
        用于第一次显示状态。使用背景色填充屏幕。
        """
        screen.fill(config.Background_color)
        #记得要调用filp，让更改可见
        pygame.display.flip()
    def display(self,screen):
        """
        用于在已经显示过一次状态再次显示。默认的行为是什么都不做。
        """
        pass
class Level(State):
    """
    游戏等级
    """
    
    def __init__(self,number=1):
        self.number=number
        #本关内还要落下多少秤砣？
        self.remaining=config.Weight_per_level
        
        speed=config.Drop_speed
        #为每个大于1的等级都增加一个speed_increase:
        speed+=(self.number-1)*config.Speed_increase
        #创建秤砣和香蕉
        self.weight=objects.Weight(speed)
        self.banana=objects.Banana()
        both=self.weight,self.banana
        self.sprites=pygame.sprite.RenderUpdates(both)
    def update(self,game):
        
        #更新所有子图形
        self.sprites.update()
        if self.banana.touches(self.weight):
            game.nextState=GameOver()
        #否则在秤砣落地时将其复位
        #如果本关内的秤砣都落下了，则切换为LevelCleared状态
        elif self.weight.landed:
            self.weight.reset()
            self.remaining-=1
            if self.remaining==0:
                game.nextState=LevelCleared(self.number)
    def display(self, screen):
        screen.fill(config.Background_color)
        updates=self.sprites.draw(screen)
        pygame.display.update(updates)

class Paused(State):
    """
    简单的暂停游戏状态，按下键盘上任意键或者点击鼠标都会结束这个状态
    """
    finished=0
    image=None
    text=''
    
    def handle(self,event):
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN,KEYDOWN]:
            self.finished=1
    def update(self,game):
        """
        更新等级
        """
        if self.finished:
            game.nextState=self.nextState()
    def firstDisplay(self, screen):
        screen.fill(config.Background_color)
        font=pygame.font.Font(None,config.font_size)
        lines=self.text.strip().splitlines()
        height=len(lines)*font.get_linesize()
        
        center,top=screen.get_rect().center
        top-=height//2
        if self.image:
            image=pygame.image.load(self.image).convert()
            r=image.get_rect()
            top+=r.height//2
            r.midbottom=center,top-20
            screen.blit(image,r)
        antialias=1
        black=0,0,0
        
        for line in lines:
            text=font.render(line.strip(),antialias,black)
            r=text.get_rect()
            r.midtop=center,top
            screen.blit(text,r)
            top+=font.get_linesize()
        pygame.display.flip()

class Info(Paused):
    nextState=Level
    text='''
    In this game you are a banana,
    trying to survive a course in 
    self-defense against fruit. where the 
    participants will "defend" themselves against 
    you with a 16 ton weight.'''
    
class StartUp(Paused):
    nextState=Info
    image=config.Splash_image
    text='''
    Welcome to Squish,
    the game of Fruit Self-Defense'''
    
class LevelCleared(Paused):
    def __init__(self,number):
        self.number=number
        self.text='''Level %i cleared 
        Click to start next level'''%self.number
    def nextState(self):
        return Level(self.number+1)
class GameOver(Paused):
    nextState=Level
    text='''
    Game Over
    Click to Restart,Esc to Quit'''
class Game:
    logging.basicConfig(level=logging.INFO,filename='mylog.log')
    def __init__(self,*args):
        logging.info(time.asctime()+'   游戏主程序初始化')
        path=os.path.abspath(args[0])
        logging.info(time.asctime()+path)
        dir=os.path.split(path)[0]
        logging.info(time.asctime()+dir)
        os.chdir(dir)
        self.state=None
        self.nextState=StartUp()
    def run(self):
        """
        初始化
        """
        logging.info(time.asctime()+'   游戏主程序开始')
        pygame.init()
        
        flag=0
        if config.full_screen:
            flag=FULLSCREEN
        screen_size=config.Screen_size
        screen=pygame.display.set_mode(screen_size,flag)
        pygame.display.set_caption('Fruti Self Denfense')
        pygame.mouse.set_visible(True)
        
        #主循环
        while True:
            if self.state!=self.nextState:
                self.state=self.nextState
                self.state.firstDisplay(screen)
            for event in pygame.event.get():
                self.state.handle(event)
            #更新状态
            self.state.update(self)
            self.state.display(screen)
            
if __name__=='__main__':
    logging.info(time.asctime()+'   载入游戏')
    game=Game(*sys.argv)
    logging.info(time.asctime()+'   开始游戏')
    game.run()