import pygame
from random import *
pygame.init()

windowsize = [400]
windowsize.append(windowsize[0])

screen = pygame.display.set_mode(windowsize)

done = False
black = [0,0,0]
white = [255,255,255]
positions = []
counter = 0

while not done:
    screen.fill(black)

    while len(positions) < 1:
        positions.append([[randint(0,399),randint(0,399)], randint(5000, 8000), [1,0]])

    for pos in positions:
        pygame.draw.circle(screen, white, pos[0], 10)
        pos[1] = pos[1] - 1 # lebensdauer
        if pos[1] == 0:
            positions.remove(pos)
            pygame.quit()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [mouse_pos[0], mouse_pos[1]]
                for pos in positions:
                    if (pos[0][0] + 10) >= mouse_pos[0] >= (pos[0][0] - 10) and (pos[0][1] + 10) >= mouse_pos[1] >= (pos[0][1] - 10):
                        positions.remove(pos)
                        counter += 1
                        print(counter)

pygame.quit()