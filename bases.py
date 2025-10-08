import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('test game')



run = True
x, y, width, height, vel = 50, 50, 40, 60, 5

while run:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT]:
        x -= vel
        
    elif keys[pygame.K_RIGHT]:
        x += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()