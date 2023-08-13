import pygame
import sys

class Menu:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.font = self.pygame.font.Font(None, 48)
        self.options = ["Iniciar Jogo", "Sair"]
        self.selected_option = 0

    def draw(self):
        self.screen.fill((0, 0, 0))  # Preenche a tela com preto
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255) if i == self.selected_option else (128, 128, 128))
            text_rect = text.get_rect(center=(self.screen.get_width() / 2, 200 + i * 100))
            self.screen.blit(text, text_rect)

    def process_events(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                sys.exit()
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_UP:
                    self.selected_option = (self.selected_option - 1) % len(self.options)
                elif event.key == self.pygame.K_DOWN:
                    self.selected_option = (self.selected_option + 1) % len(self.options)
                elif event.key == self.pygame.K_RETURN:
                    if self.selected_option == 0:
                        return "iniciar_jogo"
                    elif self.selected_option == 1:
                        sys.exit()
        return "menu"


