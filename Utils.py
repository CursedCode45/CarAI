import pygame
import os
import math
import numpy as np


# Width and Height of the window
WIDTH = 1920
HEIGHT = 1040
FPS = 60
NUMBER_OF_PLAYERS = 10


WINDOW_NAME = "Car AI"
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(WINDOW_NAME)
backgroundColor = (42, 57, 144)

road_image = pygame.transform.smoothscale(pygame.image.load('assets/road.png').convert_alpha(), (WIDTH, HEIGHT))
road_rect = pygame.surface.Surface.get_rect(road_image)

clock = pygame.time.Clock()
WALLS = []

goodPlayerWeights = [-0.4877328824596414, 0.29581985694086255, -0.19856711230553348, -0.9515133043043038, -0.1601252032803291, 0.6996188439772604, -0.5209545067962751, 0.9654379699206492, -0.24170349530272983, 0.7717047909796357, 0.3770251215290419, 0.5940716840041129, -0.9356216144969156, -0.5932617890478993, 0.7842418505483439, 0.4173276421717682, 0.26578694996407304, -0.5879535638355644, 0.5033638703975503, -0.10816875627785949, -0.6103131925812435, 0.20449173286000333, -0.022923738659964332, 0.7553215219193519, -0.7032742739593272, -0.37471929625920875, -0.41505203978637756, -0.7306059339001416, -0.07328274082636232, 0.5637035526445782, -0.5720036321759845, 0.08990602169410877, 0.03701531302179059, -0.12961063604199308, -0.6176502505695312, -0.1615422340010404, -0.377182408527611, 0.2532962313949545, -0.779076504228394, 0.6035875820978842, 0.4577443754013135, -0.3328238378668382]



def keyPresses(keys, p1):
    if keys[pygame.K_a]:
        p1.rotate(False, True)
    if keys[pygame.K_d]:
        p1.rotate(True, False)
    if keys[pygame.K_w]:
        p1.moveF()
    if keys[pygame.K_s]:
        p1.moveB()


def fillScreen():
    surface.fill(backgroundColor)


def displayText(what, where):
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render(what, True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.x += where[0]
    textRect.y += where[1]
    surface.blit(text, textRect)


def displayFPS():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("FPS: " + str(round(clock.get_fps(), 1)), True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.x += 5
    textRect.y += 5
    surface.blit(text, textRect)


class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = (0, 0, 0)
        self.lineThickness = 2

    def draw(self):
        pygame.draw.line(surface, self.color, (self.x1, self.y1), (self.x2, self.y2), width=self.lineThickness)

    def setColor(self, color):
        self.color = color

    def setLineThickness(self, thickness):
        self.lineThickness = thickness

    def hitPlayer(self, player):
        carCorners = []


def linesCollided(x1, y1, x2, y2, x3, y3, x4, y4):
    uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    if 0 <= uA <= 1 and 0 <= uB <= 1:
        return True
    return False


def getCollisionPoint(x1, y1, x2, y2, x3, y3, x4, y4):
    uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / ((y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1))
    if 0 <= uA <= 1 and 0 <= uB <= 1:
        intersectionX = x1 + (uA * (x2 - x1))
        intersectionY = y1 + (uA * (y2 - y1))
        return intersectionX, intersectionY
    return None



def drawWalls():
    for wall in WALLS:
        wall.draw()


def ReLU(x):
    return max(0, x)


# Outter Walls
WALLS.append(Wall(108, 914, 97, 790))
WALLS.append(Wall(97, 790, 124, 286))
WALLS.append(Wall(124, 286, 152, 228))
WALLS.append(Wall(152, 228, 355, 36))
WALLS.append(Wall(355, 36, 416, 12))
WALLS.append(Wall(416, 12, 682, 5))
WALLS.append(Wall(682, 5, 764, 52))
WALLS.append(Wall(764, 52, 851, 208))
WALLS.append(Wall(851, 208, 860, 266))
WALLS.append(Wall(860, 266, 831, 437))
WALLS.append(Wall(831, 437, 895, 421))
WALLS.append(Wall(895, 421, 1001, 81))
WALLS.append(Wall(1001, 81, 1094, 16))
WALLS.append(Wall(1094, 16, 1739, 46))
WALLS.append(Wall(1739, 46, 1825, 130))
WALLS.append(Wall(1825, 130, 1836, 301))
WALLS.append(Wall(1836, 301, 1766, 396))
WALLS.append(Wall(1766, 396, 1543, 447))
WALLS.append(Wall(1543, 447, 1339, 464))
WALLS.append(Wall(1339, 464, 1288, 543))
WALLS.append(Wall(1288, 543, 1295, 576))
WALLS.append(Wall(1295, 576, 1562, 517))
WALLS.append(Wall(1562, 517, 1638, 530))
WALLS.append(Wall(1638, 530, 1768, 617))
WALLS.append(Wall(1768, 617, 1807, 686))
WALLS.append(Wall(1807, 686, 1818, 833))
WALLS.append(Wall(1818, 833, 1748, 930))
WALLS.append(Wall(1748, 930, 1511, 981))
WALLS.append(Wall(1511, 981, 454, 1000))
WALLS.append(Wall(454, 1000, 207, 999))
WALLS.append(Wall(207, 999, 108, 914))


# Inner Walls
WALLS.append(Wall(284, 809, 301, 338))
WALLS.append(Wall(301, 338, 455, 193))
WALLS.append(Wall(455, 193, 630, 189))
WALLS.append(Wall(630, 189, 673, 267))
WALLS.append(Wall(673, 267, 645, 430))
WALLS.append(Wall(645, 430, 679, 572))
WALLS.append(Wall(679, 572, 792, 633))
WALLS.append(Wall(792, 633, 987, 585))
WALLS.append(Wall(987, 585, 1052, 523))
WALLS.append(Wall(1052, 523, 1155, 201))
WALLS.append(Wall(1155, 201, 1647, 225))
WALLS.append(Wall(1647, 225, 1517, 266))
WALLS.append(Wall(1517, 266, 1285, 283))
WALLS.append(Wall(1285, 283, 1213, 323))
WALLS.append(Wall(1213, 323, 1114, 471))
WALLS.append(Wall(1114, 471, 1102, 538))
WALLS.append(Wall(1102, 538, 1131, 695))
WALLS.append(Wall(1131, 695, 1236, 769))
WALLS.append(Wall(1236, 769, 1569, 704))
WALLS.append(Wall(1569, 704, 1629, 743))
WALLS.append(Wall(1629, 743, 1628, 767))
WALLS.append(Wall(1628, 767, 1492, 800))
WALLS.append(Wall(1492, 800, 285, 808))


