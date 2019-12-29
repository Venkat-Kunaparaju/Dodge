import pygame
from random import shuffle
pygame.init()

win = pygame.display.set_mode((1000,800))
boundary = pygame.Rect(0,0,1000,800)
pygame.display.set_caption("Dodge")
win_width = 1000
win_height = 800
clock = pygame.time.Clock()
run = True
WHITE = (255, 255, 255) #1
BLACK = (0, 0, 0) #2
RED = (255, 0, 0) #3
GREEN = (0, 255, 0) #4
BLUE = (0, 0, 255) #5
YELLOW = (255, 255, 0) #6
LIGHTBLUE = (0, 155, 155) #7
BROWN = (139,76,57) #8
ORANGE = (255,128,0) #9
DARKGREEN = (0,100,0)
bg = [pygame.image.load("rainbow.jpg")]
bg[0] = pygame.transform.scale(bg[0], (win_width, win_height))
class Player:
    def __init__(self):
        self.x = 500
        self.y = 500
        self.width = 10
        self.height = 10
        self.vel = 7
        self.rect = (self.x,self.y,self.width,self.height)
        self.count = 0
    def draw(self):
        self.rect = (self.x,self.y,self.width,self.height)
        pygame.draw.rect(win,DARKGREEN,self.rect)
        font = pygame.font.SysFont('robotoblack', 50)
        end = font.render(f'Score: {self.count}', 1, YELLOW)
        win.blit(end, (win_width-end.get_width(), 0))
        
    def boundaryright(self):
        if self.x + self.width + self.vel < 1000:
            return True
        else:
            return False
    def boundaryleft(self):
        if self.x - self.vel > 0:
            return True
        else:
            return False
    def boundaryup(self):
        if self.y - self.vel > 0:
            return True
        else:
            return False
    def boundarydown(self):
        if self.y + self.width + self.vel < 800:
            return True
        else:
            return False
class Game:
    def __init__(self):
        self.width = win_width
        self.height = win_height
        self.run = False
        self.reset = True
        self.face = [pygame.transform.scale(pygame.image.load("Black_colour.jpg"), (100,100))]
    def redraw(self):
        
        if not(circle.col):
            win.blit(bg[0], (0,0))
            circle.collision()
            player.draw()
            circle.draw()
            
        if circle.col:
            circle.dead()
        
        pygame.display.update() 
    def restart(self):
        player.x = 500
        player.y = 500
        circle.all_circles.clear()
        circle.col = False
        player.count = 0
    
class Circle:
    def __init__(self):
        self.dime = 100
        self.vel = [5,10,15]
        self.x = [-100,1100]
        self.y = [x*100 for x in range(0,10)]
        self.all_circles = []
        self.hitbox = []
        self.timer = 10
        self.make = True
        self.col = False
        self.deathcounter = 200
        self.death = ['You have been caught']
    def maker(self):
        if self.make:
            self.timer = 10
            self.make = False
            shuffle(self.vel)
            shuffle(self.x)
            shuffle(self.y)
            shuffle(game.face)
            self.all_circles.append([self.x[0], self.y[0], self.dime, self.vel[0], self.x[0], game.face[0]])
            
        else:
            
            if self.timer == 0:
                self.make = True
                self.timer = 10
            else:
                self.timer -= 1
    def draw(self):
        for circle in self.all_circles:
            
            
            win.blit(circle[5], (circle[0], circle[1]))
            
            if circle[4] == -100:
                circle[0] += circle[3]
            if circle[4] == 1100:
                circle[0] -= circle[3]
            circle = [circle[0], circle[1], circle[2], circle[3], circle[4], circle[5]]
            
            
            if circle[4] == -100:
                if circle[0] > 1100:
                    self.all_circles.remove(circle)
                    player.count += 1
            if circle[4] == 1100:
                if circle[0] < -100:
                    self.all_circles.remove(circle)
                    player.count += 1
    def collision(self):
        for circle in self.all_circles:
            circle = pygame.Rect(circle[0], circle[1], circle[2], circle[2])
            if circle.colliderect(player.rect):
                self.col = True
                shuffle(self.death)
                
    def dead(self):
        font = pygame.font.SysFont('robotoblack', 50 )
        end = font.render(self.death[0], 1, RED)
        win.blit(end, (win_width*.5-end.get_width()/2, 200))
        restart = font.render('Press R to try again', 1, RED)
        win.blit(restart, (win_width*.5-restart.get_width()/2, 350))
        
        
        
        
            
            
        
            

        

player = Player()
game = Game()
circle = Circle()

while game.reset:
    circle.all_circles.clear()
    game.run = True
    while game.run:
        clock.tick(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
                game.reset = False

        keys = pygame.key.get_pressed()
        if not(circle.col):
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.boundaryleft():
                player.x -= player.vel

            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.boundaryright():
                player.x += player.vel

            if (keys[pygame.K_UP] or keys[pygame.K_w]) and player.boundaryup():
                player.y -= player.vel

            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player.boundarydown():
                player.y += player.vel
        else:
            if keys[pygame.K_r]:
                game.restart()
                
        circle.maker()
        game.redraw()
    
    pygame.quit()