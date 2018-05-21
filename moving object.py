import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("MEOW")

x = 50
y = 60
width = 2
height = 20
vel = 5

start = True
while start:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel
        win.fill((0, 0, 0,)) 
        pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
        pygame.display.update()



pygame.quit()
    
