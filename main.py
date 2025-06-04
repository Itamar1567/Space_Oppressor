import pygame
import random

pygame.init()

class Bullet:
    def __init__(self, speed,startPosX, startPosY,color, screen):
        self.surface = screen
        self.speed = speed
        self.startPosX = startPosX
        self.startPosY = startPosY
        self.color = color
        self.width = 5
        self.height = 25
        self.rect = pygame.Rect(self.startPosX, self.startPosY, self.width, self.height)
    def Shoot(self):
        pygame.draw.rect(self.surface,self.color,self.rect)
        self.rect.y -= self.speed
    def GetRect(self):
        return self.rect
class Enemy:
    
    def __init__(self, screenX, screenY, radius, color, enemySpeed):
        self.screenX = screenX
        self.screenY = screenY
        self.radius = radius
        self.color = color
        self.posX = random.randint(0, screenX)
        self.posY = 0 -random.randint(50, 1000)
        self.width = 50
        self.height = 50
        self.enemyRect = None
        self.speed = enemySpeed
        
    def Spawn(self, surface):
        self.enemyRect = pygame.Rect(self.posX,self.posY, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.enemyRect) 
    def Move(self):
        self.posY += self.speed 
    def GetEnemy(self):
        return self.enemyRect;  
    def Die(self, color):
        self.color = color
    
    
class Player:
    
    def __init__(self, x, y, radius, color):
        self.score = 0
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
    
    def GetScore(self):
        return self.score 
    def SetScore(self, incrementer):
        self.score += incrementer
#Attributes
enemySpeed = 5
bulletSpeed = 15

#UI
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
font = pygame.font.SysFont('Arial', 30)
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX,screenY))
pygame.display.set_caption("Spaceship Game")
center_x = screenX//2
center_Y = screenY//2
radius = 75
border = 2

clock = pygame.time.Clock()

#Object Instantiation
player = Player(center_x,center_Y, radius, white)
enemies = []
for _ in range(15):
    new_enemy = Enemy(screenX , screenY, radius, red,enemySpeed)
    enemies.append(new_enemy)

bullets = []

enemiesToRemove = []
bulletsToRemove = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                new_bullet = Bullet(bulletSpeed,mouseX,playerShootPoint,white,screen)
                bullets.append(new_bullet)
        if event.type == pygame.QUIT:
            running = False
    mouseX, mouseY = pygame.mouse.get_pos()
    playerShootPoint = mouseY - 75
    screen.fill(black)
    for bullet in bullets:
        bullet.Shoot()
    for enemy in enemies:
        enemy.Spawn(screen)
        enemy.Move()
        enemyRect = enemy.GetEnemy()
        for new_bullet in bullets:
            if enemyRect and new_bullet.GetRect().colliderect(enemyRect):
                #Adds objects that need to be removed into their corresponding removal array
                enemiesToRemove.append(enemy)
                bulletsToRemove.append(new_bullet)
                player.SetScore(1)
                print("Collided")
                
    #object removal
    #This iterates over all objects that need to be removed, located inside nameToRemove arrays
    for enemy in enemiesToRemove:
        #if an object that is in nameToRemove then remove it from the object's array and the nameToRemove array
        if enemy in enemies:
            enemies.remove(enemy)
    enemiesToRemove.clear()
    #Remove all object to be destroyed after removing them from their arrays
    for new_bullet in bulletsToRemove:
        if new_bullet in bullets:
            bullets.remove(new_bullet)  
    bulletsToRemove.clear()
    #Function to move the player based on mouse position
    player.Move(screen,mouseX,mouseY)
    #Renders a text with the player's score
    scoreText = font.render("Score: " + str(player.GetScore()), False, white)
    #Adds the score text to the screen
    screen.blit(scoreText, (100,100))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

