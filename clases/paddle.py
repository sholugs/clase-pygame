import pygame

class Paddle(pygame.Rect):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h)
        self.speed = speed

    def move_paddle(self, ball, keys, key_up, key_down, screen_height):
        if keys[key_up]:
            self.move_ip(0, -self.speed)
        if keys[key_down]:
            self.move_ip(0, self.speed)

        if self.top < 0:
            self.top = 0
        if self.bottom > screen_height:
            self.bottom = screen_height