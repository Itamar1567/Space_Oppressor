import pygame

pygame.init()


class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    def move(self, surface, posX, posY):
        pygame.draw.circle(surface, self.color, (posX, posY), self.radius)
        
    



screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX,screenY))
pygame.display.set_caption("Spaceship Game")

white = (255,255,255)
black = (0,0,0)
center_x = screenX//2
center_Y = screenY//2
radius = 75
border = 2
player = Player(center_x,center_Y, radius, white)
clock = pygame.time.Clock()
pygame.mouse.get_cursor()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseX, mouseY = pygame.mouse.get_pos()
    screen.fill(black)
    player.move(screen,mouseX,mouseY)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()

