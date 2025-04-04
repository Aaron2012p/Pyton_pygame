import pygame as  pg
pg.init()
screen = pg.display.set_mode((800, 800))
running = True
character = pygame.image.load("icon.png")

screen.blit(image, (0, 0))
pg.display.flip()

while running:
    for event in pg.event.get():
        if pg.K_UP.get_pressed():
           pg.movecharacter() 