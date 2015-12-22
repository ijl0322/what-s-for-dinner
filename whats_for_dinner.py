import random, pygame, sys, time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600, 500))
pygame.display.set_caption("What's for dinner")

myfont = pygame.font.SysFont(None, 50)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

dinner = ["Taco Bell", "Mcdonalds", "Salad", "Chipoltle", "Wendy's",\
          "Chili's", "IN-N-OUT", "Pizza hut"]

img = pygame.image.load("slotMachine.jpg")
img.convert()
imgRect = pygame.Rect(0,0,400,421)

def quit_game(event):
    if event.type == QUIT:
        pygame.quit()
        sys.exit()    


pause = False

while True:
    for event in pygame.event.get():
        quit_game(event)
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pause = not pause

    if pause:
        continue

    go = myfont.render("Press space bar to stop or begin", True, RED)
                    
    window.fill(WHITE)
    today = random.choice(dinner)
    text = myfont.render(today, True, BLACK)
    textRect = text.get_rect()
    textRect.centerx = 180
    textRect.centery = 280
    window.blit(img, imgRect)
    pygame.draw.rect(window, BLACK, pygame.Rect(80,220,203,110))
    pygame.draw.rect(window, WHITE, pygame.Rect(85,230,60,90))
    pygame.draw.rect(window, WHITE, pygame.Rect(150,230,60,90))
    pygame.draw.rect(window, WHITE, pygame.Rect(215,230,60,90))
    window.blit(text, textRect)
    window.blit(go,(30,430))
    pygame.display.update()
    time.sleep(0.02)
    
