import pygame
from collisions import check_collision
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

# CHANGES 
# creation of door class 
# creation of a collision func on a separate file 
# doors change color if they are colliding with the player and the user press e 
# Added the player image and modified its size to (128,128) when creating the character instance  

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

        # Draw doors 
        doors_instance[0].draw(self.Screen, black, 100, 140)
        doors_instance[1].draw(self.Screen, black, 600, 140)

        # Check collisions with doors
        for door in doors_instance:
            door.collision(self.Input)

        # Draw player 
        self.Screen.blit(character.image, character.player_rect)
                
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

            self.Input = pygame.key.get_pressed()
            character.movement(self.Input)
            character.jump_motion(self.Input)


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

        # Import PLAYER IDLE
        self.player_idle_0= pygame.image.load('player_idle_0.png').convert_alpha()
        self.image= pygame.transform.scale(self.player_idle_0, (self.width, self.height))
        self.player_rect= self.image.get_rect(midbottom= (self.x, self.y))
        

    def return_rect(self):
        return self.player_rect

    def movement(self, key):
        # Moving left and right
        if key[pygame.K_a] and self.player_rect.x > 0:
            self.player_rect.x -= self.velx
        if key[pygame.K_d] and self.player_rect.x < Screen.width - self.width:
            self.player_rect.x += self.velx

    def jump_motion(self, key):
        # Explanations, JUMPING MOTION (line 1)
        if self.jump is False and key[pygame.K_SPACE]:
            self.jump = True
        if self.jump is True:
            self.player_rect.y -= self.mod_yvel * 3
            self.mod_yvel -= 1
        if self.mod_yvel < -self.yvel:
            self.jump = False
            self.mod_yvel = self.yvel
    
# Create doors 
class Doors():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Draw the door 
    def draw(self, screen, color, x, y):
        self.x = x
        self.y = y
        self.color = color 
        self.collide_color = (255,0,0)
        self.screen = screen   
        
        self.door = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 5)

    # Checks collisions 
    def collision(self, key):
        player = character.return_rect()

        # Actions to do if collisions are True 
        if check_collision(self.door, player) and key[pygame.K_e]:
            self.door = pygame.draw.rect(self.screen, self.collide_color, (self.x, self.y, self.width, self.height), 5)
        else: 
            self.door = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 5)
            

Screen = Main()
character = GenericMainCharacter(400, 300, 10, 60, 96, 8)
doors_instance = [Doors(100, 160), Doors(100, 160)]
Screen.run()