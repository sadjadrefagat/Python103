import pygame
#تغییرات شماره 3 در لوکال
from random import shuffle
#تغییرات از وب سایت داده شده است
BOXES = []
#تغییرات شماره یک در لوکال
numbers = [i+1 for i in range(16)]
#تغییرات شماره 2 در سایت
shuffle(numbers)
for row in range(4):
    for col in range(4):
        rect = (52 + col*100, 52 + row*100, 96, 96)
        number = numbers[row*4 + col]
        BOXES.append([number, rect])
        if number == 16:
            empty = row*4 + col
pygame.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont("IMPACT", 72)
loop = True
while loop:
    mX, mY = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mX, mY = pygame.mouse.get_pos()
    screen.fill((220, 255, 255))
    for i in range(16):
        if BOXES[i][0] != 16:
            rect = pygame.Rect(BOXES[i][1])
            pygame.draw.rect(screen, (0, 0, 0), rect)
            text = font.render(f"{BOXES[i][0]}", True, 'white')
            screen.blit(text, text.get_rect(center=rect.center))
            if rect.collidepoint(mX, mY):
                er, ec = empty // 4, empty % 4
                r, c = i // 4, i % 4
                if (r == er and abs(c-ec) == 1) or (c == ec and abs(r-er) == 1):
                    BOXES[i][0], BOXES[empty][0] = 16, BOXES[i][0]
                    empty = i
    pygame.display.flip()
pygame.quit()
