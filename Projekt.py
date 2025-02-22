import pygame
from random import *
pygame.init()

windowsize = [400]
windowsize.append(windowsize[0])

screen = pygame.display.set_mode(windowsize)

clock = pygame.time.Clock()

done = False
black = [0,0,0]
white = [255,255,255]
positions = []
counter = 0

while not done:
    screen.fill(black)

    while len(positions) < 1:
        direct = randint(1,100)
        if direct <= 50:
            positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [0, 0]])
        elif 50 < direct <=90:
            direct = randint(1,100)
            if direct <= 25:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [.01, 0]])
            elif 25 < direct <= 50:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [0, .01]])
            elif 50 < direct <= 75:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [- .01, 0]])
            elif 75 < direct:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [0, -.01]])
        elif 90 < direct <= 100:
            direct = randint(1, 100)
            if direct <= 25:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [.01, .01]])
            elif 25 < direct <= 50:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [-.01, .01]])
            elif 50 < direct <= 75:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [.01, -.01]])
            elif 75 < direct:
                positions.append([[randint(0, 399), randint(0, 399)], randint(5000, 8000), [-.01, -.01]])
#        positions.append([[randint(0,399),randint(0,399)], randint(5000, 8000), [.01,0]])

    for pos in positions:
        pygame.draw.circle(screen, white, pos[0], 10)
        pos[1] = pos[1] - 1 # lebensdauer
        if pos[1] == 0:
            positions.remove(pos)
            pygame.quit()
        pos[0][0] = pos[0][0] + pos[2][0]
        pos[0][1] = pos[0][1] + pos[2][1]

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