import pygame
import random

pygame.init()


class Enemy:
    
    def __init__(self, screenX, screenY, radius, color):
        self.screenX = screenX
        self.screenY = screenY
        self.radius = radius
        self.color = color
        self.posX = random.randint(0, screenX)
        self.posY = random.randint(0, screenY)
        self.width = 100
        self.height = 100
        self.enemyRect = None
        
    def Spawn(self, surface):
        self.enemyRect = pygame.Rect(self.posX,self.posY, self.width, self.height)
        pygame.draw.rect(screen,red, self.enemyRect)  
    def GetEnemy(self):
        return self.enemyRect;  
    
class Player:
    
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.width = 100
        self.height = 100
        self.playerRect = pygame.Rect(50,50,50,50)

    def Move(self, surface, posX, posY):

        self.playerRect = pygame.Rect(posX-50,posY-50, self.width, self.height)
        pygame.draw.rect(surface, self.color, self.playerRect)
        
    def GetPlayer(self):
        return self.playerRect
   


screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX,screenY))
pygame.display.set_caption("Spaceship Game")
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
center_x = screenX//2
center_Y = screenY//2
radius = 75
border = 2




player = Player(center_x,center_Y, radius, white)
clock = pygame.time.Clock()


enemies = []
for _ in range(15):
    enemy = Enemy(screenX , screenY, radius, red)
    enemies.append(enemy)
    


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill(black)
    
    for obstacle in enemies:
        enemy.Spawn(screen)
        obsRect = obstacle.GetEnemy()
        if obsRect and player.GetPlayer().colliderect(obsRect):
            obstacle.color = black
            print("Collided")
    player.Move(screen,mouseX,mouseY)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

