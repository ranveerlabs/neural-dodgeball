import pygame
import random
import math

pygame.init()
screen=pygame.display.set_mode((500,500))
clk=pygame.time.Clock()

class Ball:
    def __init__(self,radius,color):
        self.x=250
        self.y=250
        self.vx=0
        self.vy=0
        self.ay=0
        self.ax=0
        self.radius=radius
        self.color=color

class Enemies:
    def __init__(self,radius,color):
        self.bx=random.randint(10,490)
        self.by=10
        self.bvx=0
        self.bvy=0
        self.radius=radius
        self.color=color

class Game:

    def inputkeys(self):
        self.ball.ax,self.ball.ay=0,0
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.ball.ax=-self.ACELL
        if keys[pygame.K_RIGHT]:
            self.ball.ax=self.ACELL
        if keys[pygame.K_UP]:
            self.ball.ay=-self.ACELL
        if keys[pygame.K_DOWN]:
            self.ball.ay=self.ACELL

    def __init__(self):
        self.RADIUS = 10
        self.ACELL = 500.0
        self.E=0.8
        self.DRAG=1.0
        self.score=0
        self.running = True
        self.ball=Ball(10,(235, 225, 250))
        self.enemies=[Enemies(8,(165, 195, 245)), Enemies(10,(170, 230, 195)), Enemies(12,(250, 230, 160))]

    def movement(self):
        for enemy in self.enemies:
            self.dx=self.ball.x-enemy.bx #distance to player on the x axis
            self.dy=self.ball.y-enemy.by #distance to player on the y axis
            self.distance=math.sqrt((self.dx**2)+(self.dy**2)) #straight line distance to ball
            self.vdx=self.dx/self.distance*500
            self.vdy=self.dy/self.distance*500
            enemy.bvx+=(self.vdx-enemy.bvx)*1.5*self.DT
            enemy.bvy+=(self.vdy-enemy.bvy)*1.5*self.DT
            enemy.by+=enemy.bvy*self.DT
            enemy.bx+=enemy.bvx*self.DT
            enemy.bvx*=1+1.6*self.DT
            enemy.bvy*=1+1.6*self.DT

        self.ball.vx += self.ball.ax * self.DT
        self.ball.vy += self.ball.ay * self.DT
        self.ball.x += self.ball.vx * self.DT
        self.ball.y += self.ball.vy * self.DT
        self.ball.vx*=max(0,1-self.DRAG*self.DT)
        self.ball.vy*=max(0,1-self.DRAG*self.DT)

    def bounce(self):
        if self.ball.x>=490:
            self.ball.x=2*(490) -self.ball.x 
            self.ball.vx*=-self.E
        if self.ball.x<=self.ball.radius:
            self.ball.x=2*self.ball.radius-self.ball.x
            self.ball.vx*=-self.E
        if self.ball.y>=490:
            self.ball.y=2*(490) -self.ball.y
            self.ball.vy*=-self.E
        if self.ball.y<=self.ball.radius:
            self.ball.y=2*self.ball.radius-self.ball.y
            self.ball.vy*=-self.E

        for enemy in self.enemies:
            if enemy.bx>=490:
                enemy.bx=2*(490) -enemy.bx 
                enemy.bvx*=-self.E
            if enemy.bx<=enemy.radius:
                enemy.bx=2*enemy.radius-enemy.bx
                enemy.bvx*=-self.E
            if enemy.by>=490:
                enemy.by=2*(490) -enemy.by
                enemy.bvy*=-self.E
            if enemy.by<=enemy.radius:
                enemy.by=2*enemy.radius-enemy.by
                enemy.bvy*=-self.E

    def loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running=False
            
            self.DT = clk.tick(60) / 1000.0

            if self.running:
                self.score+=1

            self.inputkeys()
            self.movement()
            self.bounce()

            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 225, 255), (int(self.ball.x), int(self.ball.y)), self.ball.radius)
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 500, 500), 2)
            if math.sqrt(((self.ball.x-self.enemies[0].bx)**2)+((self.ball.y-self.enemies[0].by)**2)) <self.ball.radius+8 or math.sqrt(((self.ball.x-self.enemies[1].bx)**2)+((self.ball.y-self.enemies[1].by)**2)) <self.ball.radius+8 or math.sqrt(((self.ball.x-self.enemies[2].bx)**2)+((self.ball.y-self.enemies[2].by)**2)) <self.ball.radius+8:
                print('game over ;( score=',self.score)
                self.running=False
            pygame.draw.circle(screen, (255, 0, 0), (int(self.enemies[0].bx), int(self.enemies[0].by)), 8)
            pygame.draw.circle(screen, (0, 0, 255), (int(self.enemies[1].bx), int(self.enemies[1].by)), 8)
            pygame.draw.circle(screen, (0, 255, 0), (int(self.enemies[2].bx), int(self.enemies[2].by)), 8)
            pygame.display.flip()
        pygame.quit()
Game().loop()
