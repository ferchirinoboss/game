import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()


class Main:
    # Class containing the game loop and screen specifications
    def __init__(self):
        self.width, self.height = 800, 400
        self.Screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = 0

    def draw(self):
        # Draws everything on to screen
        self.Screen.fill(white)
        pygame.draw.rect(self.Screen, black, (0, 300, self.width, 100))
        doors.draw(self.Screen, black, 100, 150)
        doors.draw(self.Screen, black, 600, 150)
        character.draw(self.Screen, blue)
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
            character.jump_motion(Input)
            self.game_clock()
            self.draw()


class GenericMainCharacter:
    # Creates blue rectangle with movement
    def __init__(self, x, y, velocity, width, height, velY):
        self.x = x
        self.y = y
        self.velx = velocity
        self.width = width
        self.height = height
        self.jump = False
        # Modified Y velocity, and static Y velocity
        # Used to set back modified Y velocity to its original value
        self.mod_yvel = velY
        self.yvel = velY

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def movement(self, key):
        # Moving left and right
        if key[pygame.K_a] and self.x > 0:
            self.x -= self.velx
        if key[pygame.K_d] and self.x < Screen.width - self.width:
            self.x += self.velx

    def jump_motion(self, key):
        # Explanations, JUMPING MOTION (line 1)
        if self.jump is False and key[pygame.K_SPACE]:
            self.jump = True
        if self.jump is True:
            self.y -= self.mod_yvel * 3
            self.mod_yvel -= 1
        if self.mod_yvel < -self.yvel:
            self.jump = False
            self.mod_yvel = self.yvel
    
# Create doors 
class Doors:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen, color, x, y):
        pygame.draw.rect(screen, color, (x, y, self.width, self.height), 1)


Screen = Main()
doors = Doors(100, 500)
character = GenericMainCharacter(300, 260, 10, 20, 40, 8)
Screen.run()