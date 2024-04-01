import pygame
from scenemanager import SceneManager
from fallingclient import FallingClient

# pygame setup
pygame.init()

display_modes = pygame.display.list_modes()
screen = pygame.display.set_mode(display_modes[0])
clock = pygame.time.Clock()
running = True
dt = 0

sceneManager = SceneManager(300, 4, screen.get_width(), screen.get_height())
client = FallingClient("ws://localhost:8765")

def handle_events(): # poll for events
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False


while running:
    handle_events()
    screen.fill("black")
    sceneManager.draw(screen, dt)
    
    pygame.display.flip() # flip() the display to put your work on screen

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()
client.disconnect()