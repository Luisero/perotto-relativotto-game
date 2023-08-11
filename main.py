import pygame
import sys
from Entities.Ball import Ball
from Entities.ShadowBall import ShadowBall

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CENTER_POINT = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gravity sim")

clock = pygame.time.Clock()

GRAVITY = .1


ball = Ball(SCREEN_WIDTH -100, 650, 20)
ball_velocity_x = -2
ball_velocity_y = -8

higher_velocity_y = ball_velocity_y
velocity_divider = 1.2

running = True

shadow_balls = []

def draw_shadow_balls(shadow_ball_list):
    for shadow_ball in shadow_ball_list:
        shadow_ball.draw(screen, pygame)

while running:
    screen.fill('cyan')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
  #  if keys[pygame.K_LEFT]:
   #     rect.move(-5, 0)


    if ball.y >= SCREEN_HEIGHT - ball.radius:
        ball_velocity_y = higher_velocity_y / velocity_divider
        velocity_divider *= 1.05
        higher_velocity_y = ball_velocity_y

    ball_velocity_y += GRAVITY
    ball.y += ball_velocity_y 

    ball.x += ball_velocity_x
    
    draw_shadow_balls(shadow_balls)

    ball.draw(screen, pygame)

    shadow_balls.append(ShadowBall(ball.x, ball.y, 20))


    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
