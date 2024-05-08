import pygame.font
from pygame import*

init()


#змінні для розміру вікна
W = 1000
H = 700

#створення вікна
window = display.set_mode((W, H))
display.set_caption("Labirint")
display.set_icon(image.load("images/treasure.png"))

#підгін картинки по розмірам до вікна
bg = transform.scale(image.load('images/background.jpg'), (W, H))
#лічильник кадрів
clock = time.Clock()

class GameSprite(sprite.Sprite):
    #конструктор класу з властивостями
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()#створення хіт боксу(замальовка спрайту)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    #метод для малювання спрайту
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < W - self.width:
            self.rect.x += self.speed
            self.image = transform.scale(image.load("images/hero_r.png"), (self.width, self.height))
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load("images/hero_l.png"), (self.width, self.height))


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, width, height, x, y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = 'right'
    def update_r_l(self, start, end):
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

        if self.direction == 'right' and self.rect.x >= end:
            self.direction = 'left'
            self.image = transform.scale(image.load('images/cyborg_l.png'), (self.width, self.height))
        if self.direction == 'left' and self.rect.x <= start:
            self.direction = 'right'
            self.image = transform.scale(image.load('images/cyborg_r.png'), (self.width, self.height))

    def update_up(self, start, end):
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed

        if self.direction == 'down' and self.rect.y >= end:
            self.direction = 'up'
            self.image = transform.scale(image.load('images/cyborg_l.png'), (self.width, self.height))
        if self.direction == 'up' and self.rect.y <= start:
            self.direction = 'down'
            self.image = transform.scale(image.load('images/cyborg_r.png'), (self.width, self.height))



player = Player('images/hero_r.png', W - 100, 50, 80, 80, 6)
enemy1 = Enemy('images/cyborg_r.png', 300, 170, 80, 80, 4)
enemy2 = Enemy('images/cyborg_r.png', 700, 350, 60, 60, 4)
enemy1.direction = 'up'
enemy2.direction = 'up'


coin1 = GameSprite('images/coin.png', 300, 70, 100, 60, 0)
coin2 = GameSprite('images/coin.png', 100, 500, 100, 60, 0)
coin3 = GameSprite('images/coin.png', 450, 320, 100, 60, 0)

coins = sprite.Group()

coins.add(coin1)
coins.add(coin2)
coins.add(coin3)

portal1 = GameSprite('images/portal.png', 550, 300, 140, 80, 0)
portals = sprite.Group()
portals.add(portal1)


wall1 = Wall(220, 156, 252, 20, 250, 550, 150)
wall2 = Wall(220, 156, 252, 400, 20, 550, 150)
wall3 = Wall(220, 156, 252, 400, 20, 550, 20)
wall4 = Wall(220, 156, 252, 200, 20, 220, 150)
wall5 = Wall(220, 156, 252, 200, 20, 80, 400)
wall6 = Wall(220, 156, 252, 20, 350, 80, 280)
wall7 = Wall(220, 156, 252, 500, 20, 80, 610)
wall8 = Wall(220, 156, 252, 20, 150, 400, 20)
wall9 = Wall(220, 156, 252, 500, 20, 80, 20)
wall10 = Wall(220, 156, 252, 20, 350, 80, 20)
wall11 = Wall(220, 156, 252, 280, 20, 400, 400)
wall12 = Wall(220, 156, 252, 20, 150, 680, 270)
wall13 = Wall(220, 156, 252, 20, 350, 930, 170)
wall14 = Wall(220, 156, 252, 500, 20, 450, 610)
wall15 = Wall(220, 156, 252, 20, 350, 930, 280)
wall16 = Wall(220, 156, 252, 20, 350, 550, 280)

walls_lst = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16]
walls = sprite.Group()

for wall in walls_lst:
    walls.add(wall)


coins_count = 0

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish is False:
        window.blit(bg, (0, 0))

        player.reset()
        player.update()

        enemy1.reset()
        enemy1.update_up(170, 500)

        enemy2.reset()
        enemy2.update_up(170, 500)

        walls.draw(window)

        coins.draw(window)

        portals.draw(window)

        if sprite.collide_rect(player, portal1):
            font = pygame.font.Font(None, 120)
            text = font.render('Win', True, (0, 250, 0))
            text_rect = text.get_rect(center=(500, 250))
            window.blit(text, text_rect)
            finish = True

        if sprite.collide_rect(enemy1, player):
            player.rect.x = W - 100
            player.rect.y = 50
            # font = pygame.font.Font(None, 120)
            # text = font.render('You Lose', True, (250, 0, 0))
            # text_rect = text.get_rect(center=(500, 250))
            # window.blit(text, text_rect)
            # finish = True
        if sprite.spritecollide(player, coins, True):
            coins_count += 1
            if coins_count == 3:
                walls.remove(wall16)






        if sprite.spritecollide(player, walls, False):
            player.rect.x = W - 100
            player.rect.y = 50





    else:
        keys_pressed = key.get_pressed()
        if keys_pressed[K_r]:
            coins_count = 0
            player.rect.x = W - 100
            player.rect.y = 50
            walls.add(wall16)
            finish = False



    display.update()
    clock.tick(40)
