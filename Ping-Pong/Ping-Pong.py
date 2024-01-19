#Игра пинг-понг!
#Создай собственный Шутер!
from random import *
from pygame import *
import time as time2
propusk = 0
health = 3
points1 = 0
points2 = 0
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self,im,speed1,speed2,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed1 = speed1
        self.speed2 = speed2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        self.rect.y -= self.speed2
        if self.rect.y > 415:
            self.speed2 *= -1
        if self.rect.y < -30:
            self.speed2 *= -1
        self.rect.x += self.speed1
class Player1(sprite.Sprite):
    def __init__(self,im,speed,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 305:
            self.rect.y += self.speed
class Player2(sprite.Sprite):
    def __init__(self,im,speed,x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(im),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_e] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys_pressed[K_d] and self.rect.y < 305:
            self.rect.y += self.speed
player1 = Player1('Platform.png',2,0,200,50,200)
player2 = Player2('Platform.png',2,650,200,50,200)
ball = GameSprite('ball.png',1,1,350,200,100,100)
win1 = GameSprite('win1.png',0,0,230,50,300,50)
win2 = GameSprite('win2.png',0,0,230,50,300,50)
font.init()
font1 = font.Font(None,36)
player_1 = font1.render('Player1:'+str(points1),True,(0,255,0))
player_2 = font1.render('Player1:'+str(points2),True,(255,0,0))
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('phon.png'),(700,500))
FPS = 60
game = True
while game:
    window.blit(background,(0,0))
    if ball.rect.colliderect(player1.rect):
        ball.speed1 *= -1
        if abs(ball.speed1) < 3:
            znak1 = ball.speed1 / abs(ball.speed1)
            znak1 *= 0.1
            ball.speed1 += znak1
        if abs(ball.speed2) < 3:
            znak2 = ball.speed2 / abs(ball.speed2)
            znak2 *= 0.1
            ball.speed2 += znak2
    if ball.rect.colliderect(player2.rect):
        ball.speed1 *= -1
        if abs(ball.speed1) < 3:
            znak1 = ball.speed1 / abs(ball.speed1)
            znak1 *= 0.1
            ball.speed1 += znak1
        if abs(ball.speed2) < 3:
            znak2 = ball.speed2 / abs(ball.speed2)
            znak2 *= 0.1
            ball.speed2 += znak2
    if ball.rect.x < -30:
        win2.reset()
        display.update()
        time2.sleep(5)
        ball.rect.x = 350
        ball.rect.y = 200
        points2 += 1
        window.blit(player_1,(20,20))
        window.blit(player_2,(560,20))
        player_1 = font1.render('Player1:'+str(points1),True,(0,255,0))
        player_2 = font1.render('Player2:'+str(points2),True,(255,0,0))
    if ball.rect.x > 700:
        win1.reset()
        display.update()
        time2.sleep(5)
        ball.rect.x = 350
        ball.rect.y = 200
        points1 += 1
        window.blit(player_1,(20,20))
        window.blit(player_2,(560,20))
        player_1 = font1.render('Player1:'+str(points1),True,(0,255,0))
        player_2 = font1.render('Player1:'+str(points2),True,(255,0,0))
    if points1 == 3:
        win1.reset()
        sleep(20)
        game = False
    if points2 == 3:
        win2.reset()
        sleep(20)
        game = False
    player1.update()
    player1.reset()
    ball.reset()
    ball.update()
    player2.update()
    player2.reset()
    window.blit(player_1,(20,20))
    window.blit(player_2,(560,20))
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False