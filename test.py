import pygame

pygame.init()

width = 600
height = 400

black = (0, 0, 0)

game_display = pygame.display.set_mode((width, height))
game_display.fill(black)
pygame.display.set_caption("Snake Game")

pygame.quit()
quit()
