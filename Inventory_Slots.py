import pygame
class Inventory_slot():
    def __init__(self, name, pos):
        self.image = pygame.image.load(name)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.count = 0

    def render(self, display):
        text = self.font.render(str(self.count), True, (0, 0, 0))
        display.blit(self.image, self.rect)
        display.blit(text, self.rect.midright)