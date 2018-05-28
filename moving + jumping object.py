#this imports the pygame module
import pygame

#this starts/initialises the pygame module
pygame.init()

#sets a caption at the top of the pygame window
#creates the pygame window where we will perform the game
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("MEOW")

#sets the screen width to 500 pixels
screenWidth = 500

#this is where we set the basic variables of the character
x = 250
y = 400
width = 40
height = 50

#this is the velocity(how fast the object moves)
vel = 5

#some more variables
isJump = False
jumpCount = 10
left = False
right = False
wc = 0

#this is a while loop
start = True
while start:
    #the pygame version of sleep
    pygame.time.delay(100)

    #this is a for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    keys = pygame.key.get_pressed()

    #these are if statements that sense for when a specific key is pressed
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
    
    #this draws the character 
    win.fill((0, 0, 0,)) 
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()


#this calls the function that closes the pygame window
 
pygame.quit()
    
