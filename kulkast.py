import pygame
from time import sleep
from math import cos, sin, radians

pygame.init()

skärm = pygame.display.set_mode((1200,600))
kula = pygame.image.load("kula.png")
KULX = 100
KULY = 500
VINKEL = 90
v0 = 5
vx = v0*cos(radians(VINKEL))
vy = v0*sin(radians(VINKEL))
a = 0



print(vx)
kör = True
while kör:
    skärm.fill((255,255,255))
    skärm.blit(kula, (KULX, KULY))
    pygame.display.flip()

    KULX += vx
    KULY -= vy - a

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kör = False
    a += 0.025
    #sleep(0.0001)
pygame.quit()
