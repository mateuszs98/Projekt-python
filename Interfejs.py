from builtins import print
import pygame
import math
import random
from MyException import *

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
class Board:  #plansza gry
    maxSize = 10
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.field = []
        self.statusOfshootedField = False
        self.counterOfshootFields = 0
        self.saveColor = (255,255,255)
        self.rememberPositionOfShip =[]
        self.field = [[Field(i,j) for j in range(self.maxSize)] for i in range(self.maxSize)] #list comprehension

    checkSizes = lambda mx, my: True if 0 <= mx <= 9 and 0 <= my <= 9 else False   #lambda do sprawdzania rozmiaru statku

    def drawBoard(self, screen):   # rysowanie mapy gry
        for i in range(self.maxSize):
            for j in range(self.maxSize):
                self.field[i][j].drawField(screen, self.dx, self.dy, i, j)#zmiana

    def changeColorField(self,mx,my):   #ustawianie koloru naszego pola po strzale komputera

        positionmx = (mx - self.dx) // Field.size
        positionmy = (my - self.dy) // Field.size

        if (Board.checkSizes(positionmx,positionmy) == True):
            if(self.field[positionmx][positionmy].shootAgain == False):
                if(self.field[positionmx][positionmy].shootAlienShip == True):
                    self.field[positionmx][positionmy].changeColor((255,0,0))
                    self.counterOfshootFields += 1
                    self.saveColor = (255,0,0)
                    self.field[positionmx][positionmy].shootAgain = True
                else:
                    self.field[positionmx][positionmy].changeColor((0, 0, 255))
                    self.saveColor = (0, 0, 255)
                    self.field[positionmx][positionmy].shootAgain = True
            else:
                return False
        else:
            return False
        return True

    def changeColorFieldbyAlien(self,mx,my):  #ustawianie koloru pól przeciwnika po strzale
        if (Board.checkSizes(mx, my) == True):
            if (self.field[mx][my].shootShip == True):
                self.field[mx][my].changeColor((255, 0, 0))
                self.counterOfshootFields += 1
                return True
            else:
                self.field[mx][my].changeColor((0, 0, 255))
        return False


    def drawShip(self, myShip):    #rysuje statki na swojej planszy
        if not isinstance(myShip, Ship):
            raise MyException("Bledna instancja w funkcji drawShip")

        positionmx = myShip.x // Field.size
        positionmy = myShip.y // Field.size

        if (self.checkBoundaries(myShip, False) == True):
            if (myShip.setHorizontal == True):
                for i in range(0, myShip.length):
                    self.field[positionmx + i][positionmy].changeColor((153,102,204))
                    self.field[positionmx + i][positionmy].shootShip= True
                    self.field[positionmx + i][positionmy].howLongShip = myShip.length #ustawiam dlugosc statku dla informacji czy zatopiony
            else:
                for i in range(0, myShip.length):
                    self.field[positionmx][positionmy + i].changeColor((153,102,204))
                    self.field[positionmx][positionmy + i].shootShip = True
                    self.field[positionmx][positionmy + i].howLongShip = myShip.length #ustawiam dlugosc statku dla informacji czy zatopiony
            return True
        else:
            print("Nie możesz tu umieścić statku!")
            return False

    def checkBoundaries(self,myShip,alien): #sprawdzamy granice statku
        if not isinstance(myShip, Ship):
            raise MyException("Bledna instancja w funkcji checkBoundaries")
        if (alien == False):
            information = myShip.getPositionInField()
            x = information[0]
            y = information [1]
            width = information [2]
            height = information [3]
        else:
            information = myShip.getPositionInField()
            x = information[0]
            y = information[1]
            width = information[2]
            height = information[3]

        if x < 0 or x + width > 10 or y < 0 or y + height > 10:
            return False

        for i in range(x, width + x):
            for j in range(y, height + y):
                if self.field[i][j].blocked == True:
                    return False

        width = width + 1
        height = height + 1
        if x - 1 >= 0:
            if x != self.maxSize - 1 and x + width <= self.maxSize:
                width += 1
            x -= 1

        if y - 1 >= 0:
            if y != self.maxSize - 1 and y + height <= self.maxSize:
                height += 1
            y -= 1

        for i in range(x, width + x):
            for j in range(y, height + y):
                self.field[i][j].blocked = True

        return True
    def drawShipsAlien(self, currentAlienShip):  #rysowanie statków przeciwnika
        if not isinstance(currentAlienShip, AlienShip):
            raise MyException("Bledna instancja w funkcji drawShipAlien")
        if (self.checkBoundaries(currentAlienShip, True) == True):
            if (currentAlienShip.setHorizontal == True):
                for i in range(currentAlienShip.length):
                    self.field[currentAlienShip.x + i][currentAlienShip.y].changeColor((173,234,234))
                    self.field[currentAlienShip.x + i][currentAlienShip.y].shootAlienShip = True
                    self.field[currentAlienShip.x + i][currentAlienShip.y].howLongShip = currentAlienShip.length
                self.appendToArray(currentAlienShip, True)
            else:
                for i in range(0, currentAlienShip.length):
                    self.field[currentAlienShip.x][currentAlienShip.y + i].changeColor((173,234,234))
                    self.field[currentAlienShip.x][currentAlienShip.y + i].shootAlienShip = True
                    self.field[currentAlienShip.x][currentAlienShip.y + i].howLongShip = currentAlienShip.length
                self.appendToArray(currentAlienShip, False)
            return True
        else:
            return False

    def getShiplength(self,x,y):   #dlugosc statku
        return self.field[x][y].howLongShip

    def changeColorFieldonGrey(self,mx,my):  #zmiana koloru pola do zatopionego statku
        self.field[mx][my].changeColor((47,79,79))

    def checkPosition(self,x,y, list):  #sprawdzanie pozycji
        xx, yy, height, width = list
        for i in range (0, width):
            for j in range(0, height):
                if (xx + i == x and yy + j == y):
                    return True
        return False

    def changeColorShipOnGrey(self, list):  #statek zatopiony - kolor szary
        xx, yy, height, width = list
        for i in range (0, width):
            for j in range(0, height):
                self.changeColorFieldonGrey(xx + i, yy + j)

    def appendToArray(self, currentAlienShip, horizontal):  #ustawianie statków
        self.rememberPosOfOne = []
        self.rememberPosOfOne.append(currentAlienShip.x)
        self.rememberPosOfOne.append(currentAlienShip.y)

        if (horizontal == True):
            self.rememberPosOfOne.append(1)
            self.rememberPosOfOne.append(currentAlienShip.length)
        else:
            self.rememberPosOfOne.append(currentAlienShip.length)
            self.rememberPosOfOne.append(1)

        self.rememberPositionOfShip.append(self.rememberPosOfOne)

    def showAllShips(self):   #pokazywanie statków przeciwnika
        for i in range(self.maxSize):
            for j in range(self.maxSize):
                if(self.field[i][j].shootAlienShip == True and self.field[i][j].shootAgain == False):
                    self.field[i][j].changeColor((191, 191, 191))
