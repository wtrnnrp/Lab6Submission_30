import sys 
import pygame as pg
pg.init()
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.cG = 255
        self.cB = 255
        self.cR = 222
        
    def draw(self,screen):
        pg.draw.rect(screen,(self.cR,self.cG,self.cB),(self.x,self.y,self.w,self.h))

    
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
        
    def isMouseOn(self):
        if (pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[0] < self.x+self.w and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[1] < self.y + self.h):
            return True
        else:
            return False
    
    def mouseGetpressed(self):
        if (self.isMouseOn() and pg.mouse.get_pressed()[0]):
            return True
        pass

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.mouseGetpressed() :
        btn.cR = 220
        btn.cG = 220
        btn.cB = 220
    elif btn.isMouseOn():
        btn.cR = 120
        btn.cG = 200
        btn.cB = 220
    else:
        btn.cR = 255
        btn.cG = 255
        btn.cB = 222
    btn.draw(screen)
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False