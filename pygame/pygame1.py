# -*- coding: utf8 -*-

# 想要在终端运行pygame,因为要指定pyhton 32，则需要 python2.7-32 pygamw1.py

import pygame #导入pygame库
from sys import exit #向sys模块借一个exit函数用来退出程序
 
pygame.init() #初始化pygame,为使用硬件做准备
 
screen = pygame.display.set_mode((300, 200), 0, 32)
#创建了一个窗口

pygame.display.set_caption("Hello, World!!!")
#设置窗口标题
 
while True:
#主循环
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
 
    screen.fill((200,200,200))
    #将背景图画上去
 
    pygame.display.update()
    #刷新一下画面