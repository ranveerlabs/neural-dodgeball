import pygame, random, math

pygame.init()
screen=pygame.display.set_mode((500,500))
clk=pygame.time.Clock()

bvx,bvy,bvx2,bvy2,bvx3,bvy3=0,0,0,0,0,0

score=1
over=False

radius = 10
accel = 500.0
e=0.8
x, y = 250.0, 250.0
vx, vy = 0.0, 0.0

bx=random.randint(10,490)
by=10.0

bx2=random.randint(10,490)
by2=10.0

bx3=random.randint(10,490)
by3=10.0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    dt = clk.tick(60) / 1000.0

    if not over:
        score+=1

        keys = pygame.key.get_pressed()
        ax, ay = 0.0, 0.0

        if keys[pygame.K_w]:
            ay = -accel
        if keys[pygame.K_s]:
            ay = accel
        if keys[pygame.K_a]:
            ax = -accel
        if keys[pygame.K_d]:
            ax = accel

        dx=x-bx
        dy=y-by
        d=math.sqrt((dx**2)+(dy**2))
        vdx=dx/d*500
        vdy=dy/d*500
        bvx+=(vdx-bvx)*1.5*dt
        bvy+=(vdy-bvy)*1.5*dt
    
        dx=x-bx2
        dy=y-by2
        d=math.sqrt((dx**2)+(dy**2))
        vdx2=dx/d*400
        vdy2=dy/d*400
        bvx2+=(vdx2-bvx2)*1.5*dt
        bvy2+=(vdy2-bvy2)*1.5*dt

    
        dx=x-bx3
        dy=y-by3
        d=math.sqrt((dx**2)+(dy**2))
        vdx3=dx/d*300
        vdy3=dy/d*300
        bvx3+=(vdx3-bvx3)*1.5*dt
        bvy3+=(vdy3-bvy3)*1.5*dt

        by+=bvy*dt
        bx+=bvx*dt
        by2+=bvy2*dt
        bx2+=bvx2*dt
        by3+=bvy3*dt
        bx3+=bvx3*dt

        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        drag=1.0
        vx*=max(0,1-drag*dt)
        vy*=max(0,1-drag*dt)

        if x>=490:
            x=2*(490) -x 
            vx*=-e
        if x<=radius:
            x=2*radius-x
            vx*=-e
        if y>=490:
            y=2*(490) -y
            vy*=-e
        if y<=radius:
            y=2*radius-y
            vy*=-e

        if bx>=490:
            bx=2*(490) -bx 
            bvx*=-e
        if bx<=radius:
            bx=2*radius-bx
            bvx*=-e
        if by>=490:
            by=2*(490) -by
            bvy*=-e
        if by<=radius:
            by=2*radius-by
            bvy*=-e

        if bx2>=490:
            bx2=2*(490) -bx2 
            bvx2*=-e
        if bx2<=radius:
            bx2=2*radius-bx2
            bvx2*=-e
        if by2>=490:
            by2=2*(490) -by2
            bvy2*=-e
        if by2<=radius:
            by2=2*radius-by2
            bvy2*=-e

        if bx3>=490:
            bx3=2*(490) -bx3 
            bvx3*=-e
        if bx3<=radius:
            bx3=2*radius-bx3
            bvx3*=-e
        if by3>=490:
            by3=2*(490) -by3
            bvy3*=-e
        if by3<=radius:
            by3=2*radius-by3
            bvy3*=-e

        bvx*=1+1.6*dt
        bvy*=1+1.6*dt
        bvx2*=1+1.2*dt
        bvy2*=1+1.2*dt
        bvx3*=1+0.8*dt
        bvy3*=1+0.8*dt

        screen.fill((35, 38, 48))
        pygame.draw.circle(screen, (235, 225, 250), (int(x), int(y)), radius)
        pygame.draw.rect(screen, (250, 170, 180), (0, 0, 500, 500), 2)
        if math.sqrt(((x-bx)**2)+((y-by)**2)) <radius+8 or math.sqrt(((x-bx2)**2)+((y-by2)**2)) <radius+8 or math.sqrt(((x-bx3)**2)+((y-by3)**2)) <radius+8:
            over=True
            print('gam over ;( score=',score)
        pygame.draw.circle(screen, (165, 195, 245), (int(bx), int(by)), 8)
        pygame.draw.circle(screen, (170, 230, 195), (int(bx2), int(by2)), 8)
        pygame.draw.circle(screen, (250, 230, 160), (int(bx3), int(by3)), 8)
        pygame.display.flip()
pygame.quit()
