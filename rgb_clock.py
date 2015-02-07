
import pygame, sys, datetime
pygame.init()

WHITE, BLACK = (255,255,255), (0,0,0)
font = pygame.font.Font("QuarcaNormThin.otf", 100)

screen = pygame.display.set_mode([800,600])

pygame.display.set_caption("Time in Hex")
done = False
title_loc = (230,220,100,100)

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    time = datetime.datetime.now().time()
    
    string = "#"
    if time.hour < 10:
        string += "0"
    string += str(time.hour)
    if time.minute < 10:
        string += "0"
    string += str(time.minute)
    if time.second < 10:
        string += "0"
    string += str(time.second)
    
    title = font.render(string,4,WHITE)
    
    back = pygame.Color(string)
    screen.fill(back)
    
    screen.blit(title,title_loc)
    
    pygame.display.flip()
