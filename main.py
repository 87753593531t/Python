import pygame
pygame.init()

display = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Анимация')
display.fill((205, 255, 255))
for i in range(150):
    pygame.draw.rect(display, 'blue',(120+i,220-i,70,50))
    pygame.time.Clock().tick(30)
    pygame.display.update()
    display.fill((205, 255, 255))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()