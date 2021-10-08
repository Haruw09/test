import pygame
from pygame.draw import *

pygame.init()

#задаем цвета
GREEN = (23, 114, 69)
PEACH = (255, 204, 153)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# x, y - координаты левого верхнего угла третьей сверху части ствола, treewidth - "ширина" ствола, treelength - "длина" ствола
def tree(x, y, treewidth, treelength):

    # ствол
    rect(screen, GREEN, (x, y - treelength, treewidth, treelength), 0)
    rect(screen, GREEN, (x, y - 17 * treelength / 8, treewidth, treelength), 0)
    polygon(screen, GREEN, [[x + treewidth / 2, y - 18 * treelength / 8], [x - treewidth / 8, y - 9 * treelength / 4 - treewidth / 5], [x + treewidth / 2, y - 3 * treelength], [x + 9 * treewidth / 8, y - 3 * treelength + treewidth / 5]])
    aalines(screen, GREEN, True, [[x + treewidth / 2, y - 18 * treelength / 8], [x - treewidth / 8, y - 9 * treelength / 4 - treewidth / 5], [x + treewidth / 2, y - 3 * treelength], [x + 9 * treewidth / 8, y - 3 * treelength + treewidth / 5]])
    polygon(screen, GREEN, [[x + 3 * treewidth / 4, y - 25 * treelength / 8], [x + 7 * treewidth / 16, y - 25 * treelength / 8 - treewidth / 10], [x + 27 * treewidth / 16, y - 4 * treelength], [x + 2 * treewidth, y - 4 * treelength + treewidth / 10]])
    aalines(screen, GREEN, True, [[x + 3 * treewidth / 4, y - 25 * treelength / 8], [x + 7 * treewidth / 16, y - 25 * treelength / 8 - treewidth / 10], [x + 27 * treewidth / 16, y - 4 * treelength], [x + 2 * treewidth, y - 4 * treelength + treewidth / 10]])

    # листочки 5 штук
    sur = pygame.Surface([6 * treewidth, 0.8 * treelength], pygame.SRCALPHA, 32)
    sur = sur.convert_alpha()
    ellipse(sur, GREEN, (0, 0, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(sur, GREEN, (treewidth, 0.1 * treelength, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(sur, GREEN, (2 * treewidth, 0, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(sur, GREEN, (3 * treewidth, 0, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(sur, GREEN, (4 * treewidth, 0.1 * treelength, 0.6 * treewidth, 0.7 * treelength), 0)
    sur2 = pygame.transform.rotate(sur, -15)
    sur3 = pygame.transform.rotate(sur, 15)
    screen.blit(sur2, (x - 8 * treewidth, y - 3.5 * treelength))
    screen.blit(sur3, (x + 4 * treewidth, y - 3.9 * treelength))

    # листочки 3 штуки
    mur = pygame.Surface([3 * treewidth, 0.8 * treelength], pygame.SRCALPHA, 32)
    mur = mur.convert_alpha()
    ellipse(mur, GREEN, (0, 0, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(mur, GREEN, (1.2 * treewidth, 0.1 * treelength, 0.6 * treewidth, 0.7 * treelength), 0)
    ellipse(mur, GREEN, (2.4 * treewidth, 0, 0.6 * treewidth, 0.7 * treelength), 0)
    mur2 = pygame.transform.rotate(mur, -15)
    mur3 = pygame.transform.rotate(mur, 10)
    screen.blit(mur2, (x - 5 * treewidth, y - 2 * treelength))
    screen.blit(mur3, (x + 3 * treewidth, y - 2.2 * treelength))

    # ветви
    arc(screen, GREEN, (x - 17 * treewidth, y - 3.5 * treelength, 17 * treewidth, 2.3 * treelength), 0.2, 3.14 / 2, 2)
    arc(screen, GREEN, (x - 7 * treewidth, y - 2 * treelength, 7 * treewidth, 2 * treelength), 0.3, 2.5 * 3.14 / 4, 2)
    arc(screen, GREEN, (x, y - 3.8 * treelength, 18 * treewidth, 3 * treelength), 3.14 / 2, 3.14 - 0.6, 2)
    arc(screen, GREEN, (x + treewidth, y - 2.3 * treelength, 7 * treewidth, 2 * treelength), 3.14 / 3, 3.14 - 0.4, 2)


def panda(x, y, size, scr):  # x,y -координаты, size - размер, scr -пространство
    ellipse(scr, WHITE, (x - 1.8 * size, y, 1.8 * size, size), 0)

    # лапы
    def b_ell(x, y, a, b, angle, color):  # функция, рисующая эллипсы под любым углом
        lapa = pygame.Surface([a, b], pygame.SRCALPHA, 32)
        lapa = lapa.convert_alpha()
        ellipse(lapa, color, (0, 0, a, b), 0)
        lapa1 = pygame.transform.rotate(lapa, angle)
        scr.blit(lapa1, (x, y))

    polygon(scr, BLACK, [[x - size / 10, y + size / 2], [x - size / 5, y + 1.3 * size], [x - size / 2, y + 1.58 * size], [x - 0.8 * size, y + 1.28 * size]])
    b_ell(x - size * 0.57, y + size * 0.45, size * 0.37, size, -18, BLACK)
    b_ell(x - 0.95 * size, y + 0.95 * size, 0.45 * size, 0.7 * size, -52, BLACK)
    polygon(scr, BLACK, [[x - 0.8 * size, y], [x - 0.8 * size, y + size], [x - size, y + 1.3 * size], [x - 1.3 * size, y + 1.5 * size], [x - 1.4 * size, y + 1.1 * size]])
    b_ell(x - 1.7 * size, y + 0.95 * size, size * 0.4, size * 0.6, -55, BLACK)
    b_ell(x - 2.2 * size, y + 0.3 * size, size * 0.4, size * 1.1, -30, BLACK)

    # голова
    polygon(scr, WHITE, [[x - 1.2 * size, y - 0.3 * size], [x - 0.9 * size, y], [x - 0.9 * size, y + 0.8 * size], [x - 1.65 * size, y + size], [x - 1.9 * size, y]])
    b_ell(x - 1.9 * size, y - 0.38 * size, 0.74 * size, 0.2 * size, 25, WHITE)
    b_ell(x - 2 * size, y, 0.2 * size, 1 * size, 14, WHITE)
    b_ell(x - 1.7 * size, y + 0.7 * size, 0.8 * size, 0.2 * size, 15, WHITE)
    b_ell(x - 1.2 * size, y - 0.25 * size, size * 0.3, 0.55 * size, 28, BLACK)
    b_ell(x - 2.1 * size, y - 0.25 * size, size * 0.3, 0.55 * size, -20, BLACK)
    ellipse(scr, BLACK, (x - size * 1.13, y + size * 0.38, 0.34 * size, 0.34 * size))
    ellipse(scr, BLACK, (x - 1.72 * size, y + 0.9 * size, 0.3 * size, 0.17 * size))
    ellipse(scr, BLACK, (x - 1.87 * size, y + 0.45 * size, 0.28 * size, 0.34 * size))


FPS = 30
screen = pygame.display.set_mode((900, 600))
rect(screen, PEACH, (0, 0, 900, 600), 0)

tree(480, 400, 23, 90)
tree(90, 420, 12, 55)
tree(260, 440, 10, 68)
tree(800, 380, 10, 75)

panda(770, 360, 120, screen)
panda(500, 450, 60, screen)

turn = pygame.Surface([240, 220], pygame.SRCALPHA, 32)
turn = turn.convert_alpha()
panda(220, 60, 90, turn)
turnp = pygame.transform.flip(turn, True, False)
screen.blit(turnp, (50, 380))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
