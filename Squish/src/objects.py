#! /usr/bin/env/python
#! -*- encoding: utf-8 -*-

import pygame,config,os
from random import randrange

"这个模块包括Squish的游戏对象"

class SquishSprite(pygame.sprite.Sprite):
    """
    Squish 中所有的子图形的泛型超类。构造函数负责载入图像，设置自图形的rect和area属性，
    并且允许它在指定区域内进行移动。area由屏幕的大小和六百决定。
    """
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image).convert()
        self.rect=self.image.get_rect()
        screen=pygame.display.get_surface()
        shrink=-config.margin*2
        self.area=screen.get_rect().inflate(shrink,shrink)
    
class Weight(SquishSprite):
    
    """
    落下的秤砣。它使用了SquishSprite构造函数设置它的秤砣图像，并且会以给定的速度作为
    构造函数的参数来设置速度
    """
    def __init__(self,speed):
        SquishSprite.__init__(self,config.Weight_image)
        self.speed=speed
        self.reset()
    def reset(self):
        """
    将秤砣移动到屏幕顶端（视线外），放置到任何水平位置上
        """
        x=randrange(self.area.left,self.area.right)
        self.rect.midbottom=x,0
    def update(self):
        """
    根据秤砣速度将它垂直移动一段距离，并且根据它是否触及屏幕底端来设置landed属性
        """
        self.rect.top+=self.speed
        self.landed=self.rect.top>self.area.bottom
        
class Banana(SquishSprite):
    """
        绝望的香蕉。
        它使用SquishSprite构造函数设置香蕉的图像，并且会停留在屏幕底端。
        它的水平位置右当前鼠标的位置决定。
        """
    def __init__(self):
        SquishSprite.__init__(self, config.Banana_image)
        self.rect.bottom=self.area.bottom
        #在没有香蕉的部分进行填充。
        #如果秤砣移动到了这些区域，它不会
        #被判定为碰撞
        self.pad_top=config.Banana_pad_top
        self.pad_side=config.Banana_pad_side
        
    def update(self):
        """
        将banana中心点的横坐标设定为当前鼠标指针的横向坐标，并且使用rect的clamp方法
        确保Banana停留在所允许的范围内。
        """
        self.rect.centerx=pygame.mouse.get_pos()[0]
        self.rect=self.rect.clamp(self.area)
    
    def touches(self,other):
        """
                    确定香蕉是否碰触了另外的自图形
        """    
        bounds=self.rect.inflate(-self.pad_side,-self.pad_top)
        bounds.bottom=self.rect.bottom
        return bounds.colliderect(other.rect)