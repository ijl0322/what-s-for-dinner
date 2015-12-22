import random, pygame, sys, time
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("What's for dinner")

myfont = pygame.font.SysFont(None, 50)
BLACK = (0,0,0)
WHITE = (255,255,255)

dinner = ["Taco Bell", "Mcdonalds", "Healthy Food", "Chipoltle", "Wendy's",\
          "Chili's", "IN-N-OUT", "Pizza hut"]

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
                    
    window.fill(WHITE)
    today = random.choice(dinner)
    text = myfont.render(today, True, BLACK)
    window.blit(text, (100, 200))
    pygame.display.update()
    time.sleep(0.02)
    
