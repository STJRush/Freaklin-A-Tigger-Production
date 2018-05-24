import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("MEOW")

screenWidth = 500

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.wc = 0
        self.standing = True

    def draw(self,win):
        if self.wc +1  >= 27:
            self.wc = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.wc//3], (self.x,self.y))
                self.wc += 1
            elif self.right:
                win.blit(walkRight[self.wc//3], (self.x,self.y))
                self.wc += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class projectile(object):
    def __init__(self,x,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def Draw(self,win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWin():
    win.blit(bg, (0,0)) 
    freaklin.draw(win)
    for bullet in bullets:
        bullet.Draw(win)
        
    pygame.display.update()

#main loop
freaklin = player(300, 410, 64, 64)
bullets = []
start = True
while start:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if freaklin.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 6:
            bullets.append(projectile(round(freaklin.x + freaklin.width //2), round(freaklin.y + freaklin.height//2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and freaklin.x > freaklin.vel:
        freaklin.x -= freaklin.vel
        freaklin.left = True
        freaklin.right = False
        freaklin.standing = False
    elif keys[pygame.K_RIGHT] and freaklin.x < 500 - freaklin.width - freaklin.vel:
        freaklin.x += freaklin.vel
        freaklin.left = False
        freaklin.right = True
        freaklin.standing = False
    else:
        freaklin.standing = True
        freaklin.wc = 0
        
    if not (freaklin.isJump):
        if keys[pygame.K_UP]:
            freaklin.isJump = True
            freaklin.right = False
            freaklin.left = False
            freaklin.wc = 0

    else:
        if freaklin.jumpCount >= -10:
            neg = 1
            if freaklin.jumpCount < 0:
                neg = -1
            freaklin.y -= (freaklin.jumpCount ** 2) * 0.5 * neg
            freaklin.jumpCount -= 1

        else:
            freaklin.isJump = False
            freaklin.jumpCount = 10
    
    redrawGameWin()

pygame.quit()
    

