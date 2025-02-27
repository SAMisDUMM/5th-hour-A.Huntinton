import pygame
import random
import math
from pygame.locals import *

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 60, 100
BALL_RADIUS = 15
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket League Prototype")

# Load assets
car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_img.fill(BLUE)
ball_img = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
pygame.draw.circle(ball_img, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)


# Car and Ball Classes
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.angle = 0

    def move(self):
        # Basic forward/backward movement
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self):
        rotated_car = pygame.transform.rotate(car_img, self.angle)
        new_rect = rotated_car.get_rect(center=(self.x, self.y))
        screen.blit(rotated_car, new_rect)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off walls
        if self.x <= BALL_RADIUS or self.x >= WIDTH - BALL_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= BALL_RADIUS or self.y >= HEIGHT - BALL_RADIUS:
            self.speed_y = -self.speed_y

    def draw(self):
        screen.blit(ball_img, (self.x - BALL_RADIUS, self.y - BALL_RADIUS))


# Game loop
def game_loop():
    clock = pygame.time.Clock()

    car = Car(WIDTH // 2, HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Control car movement
        if keys[K_UP]:
            car.speed = 5
        elif keys[K_DOWN]:
            car.speed = -5
        else:
            car.speed = 0

        if keys[K_LEFT]:
            car.angle += 5
        elif keys[K_RIGHT]:
            car.angle -= 5

        # Move and draw objects
        car.move()
        ball.move()
        car.draw()
        ball.draw()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


# Run the game
if __name__ == "__main__":
    game_loop()