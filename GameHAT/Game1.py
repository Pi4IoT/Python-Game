import pygame
import os

# Define some colors
BLACK = (50, 50, 50)
WHITE = (200, 200, 200)
GREEN = (0, 100, 0)
RED = (100, 0, 0)

pygame.init()

screen_width=640
screen_height=480

screen=pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(None, 120)

pygame.mouse.set_visible(0)

screen.fill(WHITE)
text = font.render("Game 1 ..", True, BLACK)
text_rect = text.get_rect(center=(screen_width/3, screen_height/3))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(1000)

screen.fill(BLACK)
text = font.render("Game 1 ....", True, WHITE)
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(1000)

screen.fill(GREEN)
text = font.render("Game 1 ......", True, BLACK)
text_rect = text.get_rect(center=(screen_width/2.5, screen_height/2.5))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(1000)

screen.fill(RED)
text = font.render("Game 1 ........", True, BLACK)
text_rect = text.get_rect(center=(screen_width/3, screen_height/2))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(1000)

pygame.quit()
quit()
