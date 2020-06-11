from Interfejs import *

class Battle(Window):
    counter = 0
    pygame.init()
    pygame.display.set_caption('Okręty')

    def __init__(self):
        self.again = False
        self.resetAll()

    def resetAll(self):  #funkcja resetująca
        Battle.counter = 0
        self.alien = Alien()
        self.width = 2 * Field.size * Board.maxSize + Field.size
        self.height = Field.size * Board.maxSize + Field.size * 3
        self.widthAlienTable = Field.size * Board.maxSize + Field.size

        self.mainBoard = Board(0, 0)
        self.alienBoard = Board(self.widthAlienTable, 0)
        self.counterformedis = 0

        self.ships = [Ship(4), Ship(3), Ship(3), Ship(2), Ship(2), Ship(2),
                      Ship(1), Ship(1), Ship(1), Ship(1)]
        self.shipsAlien = [AlienShip(4), AlienShip(3), AlienShip(3), AlienShip(2), AlienShip(2), AlienShip(2),
                           AlienShip(1), AlienShip(1), AlienShip(1), AlienShip(1)]
        self.finish = False
        self.setReset = False
        self.previousFields = []
        self.alocated = [True, False, False, False]
        self.endOfGame = False
        self.yourTurn = random.randint(0, 1)

        self.screen = pygame.display.set_mode((self.width, self.height))
        if (self.again == False):
            self.gameIntro()
        else:
            self.loop()

    def gameIntro(self):   #okno strartowe
        intro = True
        BackGround = Background('tlo.png', [0,0])
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill([255, 255, 255])
            self.screen.blit(BackGround.image, BackGround.rect)

            largeText = pygame.font.SysFont('Arial', 115)
            TextSurf, TextRect = self.textObjects1("Okręty", largeText)
            TextRect.center = ((self.width / 2 +350, (self.height - 300) / 4))
            self.screen.blit(TextSurf, TextRect)

            self.button((0, 255, 0), "START", 850, 350, 150, 100, "START")
            self.button((255, 0, 0), "KONIEC", 850, 450, 150, 100, "KONIEC")



            pygame.display.update()

   def button(self, color, text, x, y, width, height, action=None):  #funkcja przycisku
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x <= mouse[0] <= x + width and y <= mouse[1] <= y + height):
            pygame.draw.rect(self.screen, color, (x, y, width, height))
            if (click[0] == 1 and action != None):
                if (action == "START"):
                    self.loop()
                elif (action == "KONIEC"):
                    pygame.quit()
                    quit()

        smallText = pygame.font.SysFont('Arial', 40)
        textSurf, textRect = self.textObjects1(text, smallText)
        textRect.center = (x + 75, y + 45)
        self.screen.blit(textSurf, textRect)

    def textObjects(self, text, font):   #tekst czarny
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def textObjects1(self, text, font):  # tekst szarawy
        textSurface = font.render(text, True, (170, 187, 204))
        return textSurface, textSurface.get_rect()

    def textObjects2(self, text, font):  # tekst szarawy, pogrubiony
        textSurface = font.render(text, True, (170, 187, 204), 'bold')
        return textSurface, textSurface.get_rect()
    
 def checkCounter(self, Board1, Board2):  #licznik dla obu plansz
        if not isinstance(Board1, Board):
            raise MyException("Bledna instancja w funkcji checkCounter")
        if not isinstance(Board2, Board):
            raise MyException("Bledna instancja w funkcji checkCounter")

        if (Board2.counterOfshootFields == 20):
            self.drawStartButton("WYGRANA", 700, 550, 200, 70)
            return True
        elif (Board1.counterOfshootFields == 20):
            self.drawStartButton("PRZEGRANA", 700, 550, 200, 70)
            return True
        else:
            return False

    def drawStartButton(self, status, x, y, width, heigth):   #przycisk start/reset w grze
        pygame.draw.rect(self.screen, (173,234,234), (x, y, width, heigth))
        smallText = pygame.font.SysFont('Arial', 40)
        textSurf, textRect = self.textObjects(status, smallText)
        if (x < 600):
            textRect.center = (x + 75, y + 35)
        else:
            textRect.center = (x + 100, y + 30)
        self.screen.blit(textSurf, textRect)

    def draw(self, screen):  # ekran podczas gry
        BackGround = Background('tlo.png', [0, 0])
        #screen.fill((0, 0, 1))
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        self.mainBoard.drawBoard(screen)
        self.alienBoard.drawBoard(screen)
        if (self.setReset == False):
            self.drawStartButton("  START", 50, 550, 175, 70)
        else:
            self.drawStartButton("   RESTART", 50, 550, 175, 70)

    def drawAlocatedShips(self):  # rysowanie naszych statków
        if (Battle.counter < 10):
            if (Battle.counter == 0):

                self.alocated[0] = False
                self.alocated[1] = True

                if (self.mainBoard.drawShip(self.ships[Battle.counter]) == False):
                    Battle.counter -= 1
            if (Battle.counter > 0 and Battle.counter < 3):
                self.alocated[1] = False
                self.alocated[2] = True
                if (self.mainBoard.drawShip(self.ships[Battle.counter]) == False):
                    Battle.counter -= 1
            if (Battle.counter >= 3 and Battle.counter <= 5):
                self.alocated[2] = False
                self.alocated[3] = True
                if (self.mainBoard.drawShip(self.ships[Battle.counter]) == False):
                    Battle.counter -= 1
            if (Battle.counter > 5 and Battle.counter <= 9):
                self.alocated[3] = True
                if (self.mainBoard.drawShip(self.ships[Battle.counter]) == False):
                    Battle.counter -= 1

    def drawAlienShips(self):  #rysowanie statków przeciwnika i ustawianie kolor takiego jak planszy
        for i in range(len(self.shipsAlien)):
            flag = True
            while (flag == True):
                if (self.alienBoard.drawShipsAlien(self.shipsAlien[i]) == False):
                    flag = True
                    self.shipsAlien[i].x = random.randint(0, 9)
                    self.shipsAlien[i].y = random.randint(0, 9)
                else:
                    flag = False

class Alien:  #gracz 2 czyli komputer
    def __init__(self):
        self.active = False
        self.temp = []
        self.counter = 0
        self.flag = False
        self.choosed = False
        self.temp1 = []
        self.previousFields = []
