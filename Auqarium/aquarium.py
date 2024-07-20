import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("aquarium simulation")

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GOLDFISH_COLOR = (255, 215, 0)
BLUEFISH_COLOR = (0, 0, 255)

class Fish:
    def __init__(self, x, y, species, color):
        self.x = x
        self.y = y
        self.species = species
        self.color = color
        self.speed = random.uniform(1, 3)

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = 0

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, 50, 20])

class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, [self.x, self.y, 20, 100])

def feed_fish(fishes):
    for fish in fishes:
        fish.speed += 0.5

fishes = [
    Fish(random.randint(0, WIDTH), random.randint(0, HEIGHT), "Goldfish", GOLDFISH_COLOR),
    Fish(random.randint(0, WIDTH), random.randint(0, HEIGHT), "Bluefish", BLUEFISH_COLOR)
]

plants = [
    Plant(100, HEIGHT - 100),
    Plant(300, HEIGHT - 100),
    Plant(500, HEIGHT - 100)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                feed_fish(fishes)

    screen.fill(BLUE)

    for plant in plants:
        plant.draw(screen)

    for fish in fishes:
        fish.move()
        fish.draw(screen)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
