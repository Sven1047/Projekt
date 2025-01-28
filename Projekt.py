import pygame
pygame.init()

windowsize = [400]
windowsize.append(windowsize[0])

screen = pygame.display.set_mode(windowsize)

done = False
black = [0,0,0]
white = [255,255,255]
positions = []

while not done:
    screen.fill(black)

    if len(positions) >= 5:
        positions.append[]

    current_i = 0
    for i in positions:

        j = i[1]
        i.pop()
        i.append(j - 1 )
        if i[1] == 0:
            positions.pop(current_i)
        current_i += 1
        print(positions)

    for pos in positions:
        pygame.draw.circle(screen, white, pos[0] , 10)

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
                mouse_pos = [[mouse_pos[0],mouse_pos[1]],10000]
                positions.append(mouse_pos)

pygame.quit()