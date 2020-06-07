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

