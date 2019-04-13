import pygame
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (640, 480)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
 
text_rotate_degrees = 0
 
for x in range(0, 300):

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [100,50], [450, 50])
    pygame.draw.line(screen, BLACK, [100,50], [100, 400])
 

    font = pygame.font.SysFont('Calibri', 70, True, False)

    text = font.render("Game 2...", True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [20, 100])

    text = font.render("Pi4IoT", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
