import pygame
import sys
from random import randint
import math
from Entities.CoinRayCast import CoinRayCast
from Entities.Ball import Ball
from Entities.ShadowBall import ShadowBall
from Entities.Coin import Coin
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CENTER_POINT = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gravity sim")

clock = pygame.time.Clock()

GRAVITY = .1


ball = Ball(SCREEN_WIDTH -100, 650, 20)
ball_velocity_x = -2
ball_acceleration_x = -.1
ball_velocity_y = -8

collide_ball_sound_path= './Assets/pop_collide.mp3'

collide_ball_sound = pygame.mixer.Sound(collide_ball_sound_path)
sound_volume = 1

sound_path = './Assets/soda_city.mp3'
sound = pygame.mixer.Sound(sound_path)
sound.play()

background_image = pygame.image.load("./Assets/background.png")  # Coloque o caminho para a sua imagem
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


higher_velocity_y = ball_velocity_y
velocity_divider = 1.2

running = True
coin = Coin(randint(0,1100), randint(0,700), 10)

coin_raycast = CoinRayCast(ball.x, ball.y, coin.x, coin.y)

coin_picked_times = -1

shadow_balls = []

shadow_balls_limit = 0

def draw_shadow_balls(shadow_ball_list):
    for index,shadow_ball in enumerate(shadow_ball_list):
        shadow_ball.draw(screen, pygame)


font = pygame.font.Font(None, 36)  # None usa a fonte padrão, 36 é o tamanho da fonte


# Posição do texto
text_x = 100
text_y = 100

image_scale_amplitude = 0

while running:
    screen.fill('black')
    time = pygame.time.get_ticks()  # Tempo decorrido desde o início do jogo
    background = pygame.transform.scale(background_image, (SCREEN_WIDTH+ math.sin(image_scale_amplitude)*2, SCREEN_HEIGHT + math.sin(image_scale_amplitude)*2))
    
    
    image_scale_amplitude += .1
    

    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        ball_acceleration_x += -.1
    if keys[pygame.K_RIGHT]:
        ball_acceleration_x += .1
    if keys[pygame.K_SPACE]:
        if ball.y < SCREEN_HEIGHT -30:
            ball_velocity_y = -8

        for index,shadow in enumerate(shadow_balls):
            
            shadow.x += randint(-10,10) / (index+1)
            
    


    if ball.y >= SCREEN_HEIGHT - ball.radius :
        ball_velocity_y *= -1
        
        collide_ball_sound.play()
        collide_ball_sound.set_volume(sound_volume)
        sound_volume *= .97
        coin_picked_times -=1


    if ball_velocity_y< 8:
        ball_velocity_y +=GRAVITY *2
    else:
        ball_velocity_y += GRAVITY

    if  ball_velocity_x >= -2 and ball_velocity_x <= 2:
        ball_velocity_x += ball_acceleration_x
    else:
        ball_velocity_x *= 0.7
        ball_velocity_x += ball_acceleration_x



    if coin_raycast.line_size < coin.radius + ball.radius:
        coin_picked_times = coin_picked_times + 1
        ball.radius*= .99
        coin.x = randint(0,1100)
        coin.y = randint(0,700)
  
    ball.y += ball_velocity_y 

    ball.x += ball_velocity_x 
    
    draw_shadow_balls(shadow_balls)

    ball.draw(screen, pygame)

    coin.draw(screen, pygame)

    coin_raycast.x1 = ball.x 
    coin_raycast.y1 = ball.y 
    coin_raycast.x2 = coin.x 
    coin_raycast.y2 = coin.y




    text_info = f'Coins: {coin_picked_times}'
    text = font.render(text_info, True, 'white')
    coin_raycast.draw(screen, pygame)


    if len(shadow_balls) > shadow_balls_limit:
        shadow_balls.pop(0)

    if shadow_balls_limit <100:
        shadow_balls_limit +=.1

    shadow_balls.append(ShadowBall(ball.x, ball.y, 20))
    screen.blit(text, (text_x, text_y))



    
    pygame.display.flip()


    clock.tick(60)

pygame.quit()
sys.exit()
