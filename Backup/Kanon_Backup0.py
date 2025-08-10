import pygame
from math import sin, cos, atan, degrees, radians
from time import sleep

pygame.init()

SKÄRMX = 1200
SKÄRMY = 600

KANONX = 99
KANONY = SKÄRMY-99

v0 = 5 # "begynnelsehastighet"

L_BLUE = (200, 200, 255)

gräs_block = pygame.image.load("gräs_block.png")
kanon_pipa_0 = pygame.image.load("kanon_pipa.png")
kanon_pipa = kanon_pipa_0
kula_b = pygame.image.load("kula.png")

kulindex = 0
kulor = []

skärm = pygame.display.set_mode((SKÄRMX,SKÄRMY))

class Kulskott:
    def __init__(self, v):
        self.x = KANONX-10
        self.y = KANONY-10
        self.vx = v0*cos(radians(v))
        self.vy = -v0*sin(radians(v))
        self.svy = 0

    def rita_kula(self):
        skärm.blit(kula_b, (self.x, self.y))

    def flytta(self):
        self.x += self.vx
        self.y += self.vy + self.svy
        self.svy += 0.025
        

def rot_center(bild, v):
    roterad_bild = pygame.transform.rotate(bild, v)
    kanon_rekt = roterad_bild.get_rect(center = bild.get_rect(center = (KANONX, KANONY)).center)
    return roterad_bild, kanon_rekt

def rita_bakgrund():
    skärm.fill(L_BLUE)
    for xkoord in range(0, SKÄRMX-18, 20):
        skärm.blit(gräs_block, (xkoord, SKÄRMY-19))

def rita_kanon_pipa():
    kanon_pipa, koord_rektangel = rot_center(kanon_pipa_0, vinkel)
    skärm.blit(kanon_pipa, koord_rektangel)
    skärm.blit(kula_b, (500,500))
    
    pygame.draw.rect(skärm, (255,0,0), (KANONX, KANONY, 1, 1))  # Röd prick för att markera "vridpunkt"
    
kör = True
while kör:
    m_pos = pygame.mouse.get_pos()
    
    if m_pos[0] != KANONX:
        vinkel = degrees(atan((KANONY-m_pos[1])/\
                 (max(m_pos[0], KANONX)-min(m_pos[0], KANONX))))
        if m_pos[0] < KANONX:
            if vinkel > 0:
                vinkel = 180 - vinkel
            else:
                vinkel = -(180 + vinkel)
    elif m_pos[1] < KANONY:
        vinkel = 90
    elif m_pos[1] > KANONY:
        vinkel = -90
    else:
        vinkel = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kör = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            kula = Kulskott(vinkel)
            kulor.append(kula)  # "Kula"-elementen "heter samma sak" fast har fortfarande inte nödvändigtvis samma värden på...
                                # ...self.vx, self.vy osv
    rita_bakgrund()  
    for k in kulor:
        if k.y < SKÄRMY-41: # SPECIFICERA EN MER NOGGRANN GRÄNS
            k.rita_kula()
            k.flytta()
        else:
            kulor.remove(k)
    rita_kanon_pipa()

    pygame.display.flip() 
    #sleep(0.01) # Eventuellt nedsaktande av skott
pygame.quit()
