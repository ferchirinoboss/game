from Instructions import steps
import pygame
pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()


class Main:
    # Class containing the game loop and screen specifications
    def __init__(self):
        self.width, self.height = 800, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = 0

    def draw(self):
        # Draws everything on to screen
        self.screen.fill(white)
        pygame.draw.rect(self.screen, black, (0, 300, self.width, 100))
        character.draw()
        clock.tick(60)
        pygame.display.update()

    def game_clock(self):
        # Creates a variable that counts fps
        self.clock += 1
        if self.clock >= 60:
            self.clock = 0

    def run(self):
        # Contains game loop
        while self.running is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            Input = pygame.key.get_pressed()

            character.movement(Input)
            self.game_clock()
            self.draw()


class Animated:
    # Creates character that follows a set list of movements
    def __init__(self, x, y, velocity, width, height, velY):
        self.velx = velocity
        self.width = width
        self.height = height
        self.jump = False

        # Player image
        self.player_idle_0 = pygame.image.load('player_idle_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.player_idle_0, (self.width, self.height))

        # Player hitbox
        self.player = self.image.get_rect(midbottom=(x, y))

    # All these variables are used in Instructions.py
        # Modified Y velocity, and static Y velocity
        # Used to set back modified Y velocity to its original value
        self.mod_yvel = velY
        self.yvel = velY

        # This creates a dictionary with multiple variables without having to define each one.
        # Creates one for each animation to know if its running, and creates a timer for each one too.
        self.animationNum = {i: False for i in range(0, 5)}
        self.timer = {i: False for i in range(0, 5 )}

        # Used to make character jump only once
        self.once = False

        # Runs Instruction.py
        self.begin = False

    def draw(self):
        # Player
        Screen.screen.blit(self.image, self.player)

        # Player hitbox left side, where x and y are positioned
        pygame.draw.line(Screen.screen, red, (self.player.x, self.player.y),
                         (self.player.x, self.player.y + 96), 5)

        # Player hitbox
        pygame.draw.rect(Screen.screen, blue, self.player, 1)

    def movement(self, key):
        # Sets of instructions.py
        if key[pygame.K_SPACE] and self.begin is False:
            # Begins with first animation
            self.animationNum[0] = True
            self.begin = True

        if self.begin is True:
            steps(self)


Screen = Main()
character = Animated(400, 300, 10, 60, 96, 8)
Screen.run()
