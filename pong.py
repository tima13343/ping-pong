from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,size_x,size_y,p_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 455:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 455:
            self.rect.y += self.speed

window = display.set_mode((600,500))
window.fill((200,255,255))

game = True
clock = time.Clock()

speed_x = 3
speed_y = 3

# создаем спрайты для игры
racket1 = Player("racket.png",30,200,4,50,10)
racket2 = Player("racket.png",520,200,4,50,10)
ball = Player("ball.png",200,200,25,25,50)

# создаем надписи
font.init()
font = font.Font(None,35)
lose1 = font.render("PLAYER 1 LOSE!",True,(180,0,0))
lose2 = font.render("PLAYER 2 LOSE!",True,(180,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if game == True:
        window.fill((200,255,255))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y 

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *=1
        if ball.rect.y > 500-50 or ball.rect.y < 0:
             speed_y *= -1

        if ball.rect.y < 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True


        if ball.rect.x > 600:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(60)
