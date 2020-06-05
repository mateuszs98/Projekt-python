from builtins import print
import pygame

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