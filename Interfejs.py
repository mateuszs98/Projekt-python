from builtins import print
import pygame
import math
import random


class Window:
    def button(self):
        print('Metoda wirtualna 1')


class Background(pygame.sprite.Sprite):  #obsługa tła
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Field:

    size = 50
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (173,234,234)
        self.blocked = False
        self.shootShip = False
        self.shootAlienShip = False
        self.shootAgain = False
        self.howLongShip = 0

    def drawField(self, screen, dx, dy,x,y):  #rysowanie pola
        pygame.draw.rect(screen, self.color, pygame.Rect(x * Field.size + dx, y * Field.size + dy, Field.size - 1, Field.size - 1))

    def changeColor(self, color):  #ustawianie koloru
        self.color = color
        
class Ship:

    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.length = length
        self.color = (153,102,204)
        self.setHorizontal = True
        self.xcoordinate = 0
        self.ycoordinate = 0

    def setPosition(self,mx,my,screen): #wybieranie pozycji dla statku
        self.x = mx
        self.y = my
        if self.setHorizontal == True:
            self.drawShipHorizontal(screen)
        else:
            self.drawShipVertical(screen)

    def getPositionInField(self):  #ustalanie pozycji na planszy
        coordinates = []
        self.xcoordinate = math.floor(self.x / Field.size)
        self.ycoordinate = math.floor(self.y / Field.size)
        coordinates.append(self.xcoordinate)
        coordinates.append(self.ycoordinate)

        if (self.setHorizontal == True):
            coordinates.append(self.length)
            coordinates.append(1)
        else:
            coordinates.append(1)
            coordinates.append(self.length)
        coordinates.append(self.setHorizontal)
        return coordinates

    def drawShipHorizontal(self,screen):
        self.setHorizontal = True
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, Field.size*self.length, Field.size))

    def drawShipVertical(self, screen):
        self.setHorizontal = False
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, Field.size, Field.size* self.length))

class AlienShip(Ship):    #klasa dziedzicząca po Ship

    def __init__(self, length):
            super().__init__(length)
            self.x = random.randint(0, 9)
            self.y = random.randint(0, 9)
            self.randHorizontal = random.randint(0, 1)
            if (self.randHorizontal == 0):
                self.setHorizontal = True
            else:
                self.setHorizontal = False

    def getPositionInField(self):  # ustalanie pozycji na planszy
        coordinates = []
        coordinates.append(self.x)
        coordinates.append(self.y)

        if (self.setHorizontal == True):
            coordinates.append(self.length)
            coordinates.append(1)
        else:
            coordinates.append(1)
            coordinates.append(self.length)
        coordinates.append(self.setHorizontal)

        return coordinates
