import pygame
import random

# pygame setup
pygame.init()

display_modes = pygame.display.list_modes()
screen = pygame.display.set_mode(display_modes[0])

clock = pygame.time.Clock()
running = True
dt = 0
numStars = 300
numColors = 4

def generate_star(i):
    return {"pos": pygame.Vector2(random.randint(0, screen.get_width()) , random.randint(0, screen.get_height())),
    "layer": random.randint(0, numColors-1)}

def generate_color(i):
    return pygame.Color(156 + (20 * i), 24 + (24 * i), 96 + (32 * i))

stars = [ generate_star(i) for i in range(numStars) ]
colors = [ generate_color(i) for i in range(numColors) ]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for i in range(numStars):
        layer = stars[i]["layer"]
        pygame.draw.circle(screen, colors[layer], stars[i]["pos"], (1 + layer) / 2)
        stars[i]["pos"].y += (5 * dt) + (layer * dt * 10)

        if stars[i]["pos"].y > screen.get_height():
            stars[i]["pos"].y = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()