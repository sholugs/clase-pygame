from clases.paddle import Paddle
from clases.ball import Ball
import pygame
import sys

def main():
    pygame.init()
    pygame.mixer.init()

    global screen_width, screen_height
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))

    paddle_width, paddle_height = 15, 80
    paddle_speed = 2
    paddle1 = Paddle(screen_width // 4, screen_height // 2, paddle_width, paddle_height, paddle_speed)
    paddle2 = Paddle(screen_width * 3 // 4, screen_height // 2, paddle_width, paddle_height, paddle_speed)

    ball = Ball(screen_width // 2, screen_height // 2, 15, 15, 2, 2)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        keys = pygame.key.get_pressed()

        paddle1.move_paddle(ball, keys, pygame.K_w, pygame.K_s, screen_height)
        paddle2.move_paddle(ball, keys, pygame.K_UP, pygame.K_DOWN, screen_height)

        ball.move_ball()
        ball.check_collision(paddle1, paddle2, screen_height)

        goal = ball.check_goal(paddle1, paddle2, screen_width)
        if goal:
            print(f"Player {goal} wins!")
            pygame.quit()
            sys.exit()

        pygame.draw.rect(screen, (255, 255, 255), paddle1)
        pygame.draw.rect(screen, (255, 255, 255), paddle2)
        pygame.draw.ellipse(screen, (255, 255, 255), ball)
        pygame.draw.aaline(screen, (255, 255, 255), (screen_width // 2, 0), (screen_width // 2, screen_height))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()