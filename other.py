import pygame
import time
from random import randint
pygame.init()
clock = pygame.time.Clock()
back = (0, 225, 200)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)


BLACK = (0, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
RED = (225, 0, 0)

platform_x = 200
platform_y = 330
speed_x = 3
speed_y = 3

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height )
        self.fill_color = back
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def colliderect(self, rect) :
        return self.rect.colliderect(rect)
        
class Label(Area):
    def set_text(self, text, fsize=16, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color) 
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x +shift_x, self.rect.y + shift_y)) 
          
class Picture(Area):
    def __init__(self, filename ,  x=0, y=0, width=10, height=10 ):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)


    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

Ball = Picture('ball.png', 200, 280, 50, 50)

platform = Picture('platform.png', platform_x, platform_y, 100, 30)
game_over = False
move_right = False
move_left = False
start_x = 5
start_y = 5
count = 9
monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j)

    for i in range(count):
        d = Picture('enemy.png', x , y, 50, 50)
        monsters.append(d)
        x = x + 50
    count = count - 1


while not game_over:
    Ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
               move_right = True
               move_left = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
               move_right = False
   

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               move_left = True
               move_right = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
               move_left = False
    if move_left: 
       platform.rect.x -=5

    if move_right: 
       platform.rect.x +=5

    Ball.rect.x += speed_x
    Ball.rect.y += speed_y
    if Ball.rect.colliderect(platform.rect):
        speed_y *= -1
    if Ball.rect.y < 0 :
       speed_y *= -1
    if Ball.rect.x > 450 or Ball.rect.x < 0 :
        speed_x *= - 1

    if Ball.rect.y > (platform_y + 20):
        time_text = Label(140, 150, 50, 50, back)
        time_text.set_text(' YOU LOSE', 60,(255, 0, 0))
        time_text.draw(10, 10)
        game_over =True


    for m in monsters:
        m.draw()
        if m.rect.colliderect(Ball.rect):
            monsters.remove(m)
            m.fill()
            speed_y  *= -1

            if len (monsters) == 0 :
               time_text = Label(140, 150, 50, 50, back)
               time_text.set_text('YOU WIN', 60,(255, 0, 0))
               time_text.draw(10, 10)
               game_over =True


                

    platform.draw()
    Ball.draw()


    pygame.display.update()
    clock.tick(40)