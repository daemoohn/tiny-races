import pygame
pygame.init()

screen = pygame.display.set_mode([1024, 800])
pygame.display.set_caption("Tiny races")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 0))
    pygame.display.flip()

pygame.quit()
