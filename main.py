import pygame
pygame.init()
width, height = 500, 500
Screen = pygame.display.set_mode((width, height))

running = True

while running is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.update()
