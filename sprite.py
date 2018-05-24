import pygame
pygame.init():
    def main():
        background = pygame.surface((640,480))
        background.fill((0,0,0))
        for i in range (1,320,3):
            pygame.draw.circle(background,(0xFF,0x00,0x00),(i,i),i,1)
            pygame.draw.circle(background,(0x00,0x00,0xFF),(640-,i),i,1)
            pygame.draw.circle(background,(0x00,0x00,0xFF),(i,480-i),i,1)
            pygame.draw.circle(background,(0xFF,0x00,0x00),(640-1,480-i),i,1)
            pygame.draw.circle(background,(0xFF,0xFF,0xFF),(320,240),i,1)
        pygame.image.save(background,"circles.bmp")
        print "look in current directory"
    if__name__ == "__main__":
        main()
            
