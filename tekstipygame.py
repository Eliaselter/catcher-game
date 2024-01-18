
import pygame as pg
import sys
import random

# Konstanter
WIDTH = 400
HEIGHT = 600

SIZE = (WIDTH, HEIGHT)

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GREY = (150,150,150)
LIGHTBLUE = (120,120,255)

pg.init()

surface = pg.display.set_mode(SIZE)

clock = pg.time.Clock()

run = True




w = 60
h = 80
x = WIDTH/2
y = HEIGHT - h

player_img = pg.image.load('bucket.png')
background_img = pg.image.load('background_snow_2-3.png')
background_img = pg.transform.scale(background_img, SIZE)

font = pg.font.SysFont('ARIAL',26)
poeng = 0
liv = 3
def displayPoints():
    text_img = font.render(f"Antall poeng: {poeng}", True, BLACK)
    surface.blit(text_img, (20,10))
def displayLiv():
    text_img = font.render(f"Antall liv: {liv}", True, BLACK)
    surface.blit(text_img, (20,35))

# class Player:
#     def __init__(self)
# class Ball:
#     def __init__(self, hball, wball, xball, yball):
#         self.hball = hball
#         self.wball = wball
#         self.xball = xball
#         self.yball = yball

class Ball:
    def __init__(self):
        self.r = 10
        self.x = random.randint(1,WIDTH-1)
        self.y = -self.r
        
    def update(self):
        self.y += 5
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x, self.y),self.r)
        #surface.blit(player_img,((self.x, self.y),self.r))

ball = Ball()

while run:
    clock.tick(FPS)
    
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    surface.blit(background_img,(0,0))
    
    vx = 0
    
    keys = pg.key.get_pressed()
    
#     ball = Ball()
    
    
        
     
    
        
    if keys[pg.K_LEFT]:
        vx = -5
    elif keys[pg.K_RIGHT]:
        vx = 5
    
    if x >= WIDTH-w:
        vx = -1
        
    if x <= 0:
        vx = 1
        
    
        
    
    x += vx
    
    ball.update()
    ball.draw()

    #pg.draw.rect(surface,GREY,[x,y,w,h])
    surface.blit(player_img, (x,y))    
    displayPoints()
    displayLiv()
    
    
        #print("Kollisjon!")
        
    
    if y < ball.y < y+h and x < ball.x < x+w:
         poeng += 1
         ball = Ball()
    elif ball.y == HEIGHT and liv > 0:
        liv -= 1
        ball = Ball()
    elif liv == 0:
        run = False
        print(f"Du fikk {poeng} Poeng")
    
    
        
    
    
         
        # Lager ny ball
        
    
        
        
    
    
    pg.display.flip()


pg.quit()
sys.exit()

