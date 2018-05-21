import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("MEOW")

screenWidth = 500

x = 250
y = 400
width = 40
height = 50
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
wc = 0


start = True
while start:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    
    win.fill((0, 0, 0,)) 
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()



pygame.quit()
    
