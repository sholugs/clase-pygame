import pygame

class Ball(pygame.Rect):
    def __init__(self, x, y, w, h, dx, dy):
        super().__init__(x, y, w, h)
        self.dx = dx
        self.dy = dy

    def move_ball(self):
        self.move_ip(self.dx, self.dy)

    def check_collision(self, paddle1, paddle2, screen_height):
        if self.colliderect(paddle1) or self.colliderect(paddle2):
            self.dx *= -1
        if self.top <= 0 or self.bottom >= screen_height:
            self.dy *= -1

    def check_goal(self, paddle1, paddle2, screen_width):
        if self.right <= 0:
            return 1  # Player 1 wins
        if self.left >= screen_width:
            return 2  # Player 2 wins
        return 0