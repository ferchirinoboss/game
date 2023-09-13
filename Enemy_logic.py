import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

# Changes to Main:
# Creation of an enemy with a field of view (FOV)
# Creation of a character hitbox
# If player gets inside the FOV, enemy will change color, increase velocity, and move in a larger area
# If enemy hits the player, game loop ends


def calls(Input):
    # Function containing all calls that must be inside game loop
    enemy.move()
    enemy.detected()
    character.movement(Input)
    character.jump_cooldown()
    character.fall()
    character.jump_motion(Input)
    Screen.game_clock()
    Screen.draw()


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
        character.draw(self.Screen, blue)
        enemy.draw(self.Screen)
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
            calls(Input)


class GenericMainCharacter:
    # Creates blue rectangle with movement
    def __init__(self, x, y, velocity, width, height, velY):
        self.x = x
        self.y = y
        self.velx = velocity
        self.velxholder = velocity
        self.width = width
        self.height = height
        self.jump = False
        self.mod_yvel = velY
        self.yvel = velY
        self.jumpCD = 0
        self.cooldown = False
        self.fell = False
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def movement(self, key):
        # Moving left and right
        if key[pygame.K_a] and self.x > 0:
            self.x -= self.velx
        if key[pygame.K_d] and self.x < Screen.width - self.width:
            self.x += self.velx

        # Puts hitbox into loop so it moves with the character
        self.hitbox = (self.x, self.y, self.width, self.height)

    def fall(self):
        # Slows down character for a few frames after jump
        if self.fell is True:
            self.velx = 0
        if self.velx < self.velxholder:
            self.velx += 0.2
        self.fell = False

    def jump_cooldown(self):
        # Sets a cooldown of 60 frames to the jump
        if self.cooldown is True:
            self.jumpCD += 1
            if self.jumpCD >= 60:
                self.jumpCD = 0
                self.cooldown = False

    def jump_motion(self, key):
        # Explanations, JUMPING MOTION (line 1)
        if self.jump is False and key[pygame.K_SPACE] and self.cooldown is False:
            self.jump = True
            self.cooldown = True
        if self.jump is True:
            self.y -= self.mod_yvel * 3
            self.mod_yvel -= 1
        if self.mod_yvel < -self.yvel:
            self.jump = False
            self.fell = True
            self.mod_yvel = self.yvel


class SmartEnemy:
    # Enemy that has a FOV and once character is inside of it, it gets angry
    def __init__(self, x, y, width, height, velocity):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.velx = velocity
        self.right, self.left = False, False
        self.FOV = []
        self.alerted = False
        self.color = green
        self.limit = Screen.width // 2

    def draw(self, screen):
        self.detection()
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        # Moves character left and right, it changes direction when it collides with the middle and the right border
        self.x += self.velx
        if self.x <= self.limit:
            self.velx *= -1

        if self.x >= Screen.width - self.width:
            self.velx *= -1

        if self.velx > 0:
            self.right = True
            self.left = False

        if self.velx < 0:
            self.right = False
            self.left = True

    def detection(self):
        # Hitboxes must be defined for each new enemy, because they depend on the size
        # Defines FOV and moves it with character
        if self.alerted is False:
            if self.right:
                self.FOV = (self.x + 21, self.y - 20, 100, 60)
            if self.left:
                self.FOV = (self.x - 100, self.y - 20, 100, 60)

        # Detects if character is in FOV
        if enemy.FOV[0] < character.x < enemy.FOV[0] + enemy.FOV[2] and enemy.FOV[1] < \
                character.y < enemy.FOV[1] + enemy.FOV[3]:
            self.alerted = True

    def detected(self):
        # Changes enemy color, gives it more space to move, and increases velocity
        if self.alerted is True:
            self.color = red
            self.limit = 0
            if self.right:
                self.velx = 5
                self.FOV = (self.x + 21, self.y - 60, 200, 120)
            if self.left:
                self.velx = -5
                self.FOV = (self.x - 200, self.y - 60, 200, 120)

        # Detects if enemy hits character, stops game loop
        if character.hitbox[0] < enemy.x < character.hitbox[0] + character.hitbox[2] and character.hitbox[1] <\
                enemy.y + 20 < character.hitbox[1] + character.hitbox[3]:
            Screen.running = False


Screen = Main()
enemy = SmartEnemy(500, 260, 20, 40, 3)
character = GenericMainCharacter(300, 260, 7, 20, 40, 8)
Screen.run()
