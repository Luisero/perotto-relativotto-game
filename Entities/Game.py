
from .CoinRayCast import CoinRayCast
from .Ball import Ball
from .ShadowBall import ShadowBall
from .Coin import Coin
import os
import math
from random import shuffle, randint

class Game:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    CENTER_POINT = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    GRAVITY = .05

    running = True

    coin_picked_times = -1


    def __init__(self, pygame) -> None:
        pygame.init()
        pygame.mixer.init()
        self.pygame = pygame 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.pygame.display.set_caption("Perotto Relativotto")

        self.clock = pygame.time.Clock()

    def load_ball(self):
        self.ball = Ball(self.SCREEN_WIDTH -100, 650, 20)
        self.ball_velocity_x = -2
        self.ball_acceleration_x = -.1
        self.ball_velocity_y = -8
        self.higher_velocity_y = self.ball_velocity_y


    def move_ball_left(self):
        self.ball_acceleration_x += -.1


    def move_ball_right(self):
        self.ball_acceleration_x += .1

    def jump_ball(self):
        if self.ball.y < self.SCREEN_HEIGHT - self.ball.radius:
            self.ball_velocity_y = -8

    def check_ball_collided(self):
        if self.ball.y >= self.SCREEN_HEIGHT - self.ball.radius :
            self.ball_velocity_y *= -1
            self.running = False
        
    def ball_is_max_velocity_y(self):
        if self.ball_velocity_y < self.higher_velocity_y:
            return True 
        else:
            return False
    
    def is_ball_on_max_velocity_x(self):
        if  self.ball_velocity_x >= -2 and self.ball_velocity_x <= 2:
            return True 
        else:
            return False

    def apply_ball_velocity_x(self):
        if  self.is_ball_on_max_velocity_x():
            self.ball_velocity_x += self.ball_acceleration_x
        else:
            self.ball_velocity_x *= 0.7
            self.ball_velocity_x += self.ball_acceleration_x


    def update_ball_position(self):
        self.ball.y += self.ball_velocity_y 

        self.ball.x += self.ball_velocity_x 

    def draw_ball(self):
        self.ball.draw(self.screen, self.pygame)


    def aplly_gravity(self):
        if self.ball_is_max_velocity_y():
            self.ball_velocity_y += self.GRAVITY *2
        else:
            self.ball_velocity_y += self.GRAVITY  
        
    def increase_gravity(self):
        if self.GRAVITY:
                self.GRAVITY += .1

    def check_coin_is_picked(self):
            
        if self.coin_raycast.line_size < self.coin.radius + self.ball.radius:
           return True 
        else:
            return False 
        
    def increase_coin_picked_times(self):
        self.coin_picked_times += 1

    def spawn_coin_in_random_point(self):
            
            self.ball.radius*= .99
            self.coin.x = randint(0,1100)
            self.coin.y = randint(0,700)
            self.shadow_balls_limit +=1
            if self.shadow_balls_radius<20:
                self.shadow_balls_radius += 1
            
            
    
    
    def load_sound_effects(self):

        self.collide_ball_sound_path= './Assets/pop_collide.mp3'

        self.collide_ball_sound = self.pygame.mixer.Sound(self.collide_ball_sound_path)
        self.sound_volume = 1
    
    def play_songs(self):

        self.music_directory = './Assets/classical_songs'

        self.music_files = [os.path.join(self.music_directory, filename) for filename in os.listdir(self.music_directory) if filename.endswith(".mp3")]
        shuffle(self.music_files)

        self.current_track = 0
        self.pygame.mixer.music.load(self.music_files[self.current_track])

        # Reproduzir música
        self.pygame.mixer.music.play()
    
    def load_background_image(self):
        self.image_scale_amplitude = 1
        self.background_image = self.pygame.image.load("./Assets/background.png")  # Coloque o caminho para a sua imagem
        self.background_image = self.pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
    
    def draw_background_image(self):
        self.background = self.pygame.transform.scale(self.background_image, (self.SCREEN_WIDTH+ math.sin(self.image_scale_amplitude)*2, self.SCREEN_HEIGHT + math.sin(self.image_scale_amplitude)*2))
        self.screen.blit(self.background, (0,0))

    def increase_image_scale_amplitude(self):
        self.image_scale_amplitude += .1

    def load_coin(self):
        self.coin = Coin(randint(0,1100), randint(0,700),10)

    def draw_coin(self):
        self.coin.draw(self.screen, self.pygame)

    def load_coin_raycast(self):
        self.coin_raycast = CoinRayCast(self.ball.x, self.ball.y, self.coin.x, self.coin.y)

    def update_coin_raycast(self):
        self.coin_raycast.x1 = self.ball.x 
        self.coin_raycast.y1 = self.ball.y 
        self.coin_raycast.x2 = self.coin.x 
        self.coin_raycast.y2 = self.coin.y

    def draw_coin_raycast(self):
        self.coin_raycast.draw(self.screen, self.pygame)


    def load_shadow_balls(self):
        self.shadow_balls = []
        self.shadow_balls_radius = 20
        self.shadow_balls_limit = 0


    def draw_shadow_balls(self,shadow_ball_list):

        for index,shadow_ball in enumerate(shadow_ball_list):
            shadow_ball.draw(self.screen, self.pygame)

    def has_max_shadow_balls(self):
        if len(self.shadow_balls) > self.shadow_balls_limit:
            return True
        else:
            return False
        
    def remove_shadow_balls(self):
        
        if self.has_max_shadow_balls and len(self.shadow_balls) != 0:
            self.shadow_balls.pop(0)

    def add_shadow_balls(self):
        self.shadow_balls.append(ShadowBall(self.ball.x, self.ball.y, self.shadow_balls_radius))

    

    def load_text(self):
        self.font = self.pygame.font.Font(None, 36)  # None usa a fonte padrão, 36 é o tamanho da fonte
        self.text_x = 100
        self.text_y = 100

    def update_text(self):

        self.text_info = f'Coins: {self.coin_picked_times}'
        self.text = self.font.render(self.text_info, True, 'white')
    
    def draw_text(self):
        self.screen.blit(self.text, (self.text_x, self.text_y))


    def get_pygame_events(self):
        return self.pygame.event.get()
           

    def change_song_if_is_busy(self):
         if not self.pygame.mixer.music.get_busy():
            self.current_track = (self.current_track + 1) % len(self.music_files)
            self.pygame.mixer.music.load(self.music_files[self.current_track])
            self.pygame.mixer.music.play()

    def get_pressed_keys(self):
        return self.pygame.key.get_pressed()
    
    

    def setup(self):
        self.load_ball()
        self.load_sound_effects()
        self.play_songs()
        self.load_background_image()
        self.load_coin()
        self.load_coin_raycast()
        self.load_shadow_balls()
        self.load_text()
     


    def loop(self):
        while self.running:
            self.screen.fill('black')
            self.time = self.pygame.time.get_ticks()  
            self.draw_background_image()
            self.increase_image_scale_amplitude()

            for event in self.get_pygame_events():
                if event.type == self.pygame.QUIT:
                    self.running = False 
                
            keys = self.get_pressed_keys()

            
            if keys[self.pygame.K_LEFT]:
                self.move_ball_left()
            if keys[self.pygame.K_RIGHT]:
                self.move_ball_right()
            if keys[self.pygame.K_SPACE]:
                self.jump_ball()
                for index,shadow in enumerate(self.shadow_balls):
                    
                    shadow.x += randint(-10,10) / (index+1)
                
            self.check_ball_collided()
            self.aplly_gravity()


            
            if self.check_coin_is_picked():
                self.spawn_coin_in_random_point()
                self.increase_gravity()
                self.increase_coin_picked_times()
                self.shadow_balls_limit +=1 
            


            self.update_ball_position()
            self.apply_ball_velocity_x()
            
            self.draw_shadow_balls(self.shadow_balls)

            self.draw_ball()
            self.draw_coin()
            self.update_coin_raycast()
            self.draw_coin_raycast()

            self.update_text()
            self.draw_text()

            self.remove_shadow_balls()
            self.add_shadow_balls()            


            self.pygame.display.flip()


            self.clock.tick(60)


    def run(self):
        self.setup()
        self.loop()

if __name__ == '__main__':
    import pygame
    game = Game(pygame)
    game.run()