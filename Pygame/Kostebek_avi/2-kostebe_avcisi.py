import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

mole_move_interval = 700  # in milliseconds, e.g., 1000 ms = 1 second

# Set the title of the window
pygame.display.set_caption("Köstebek oyunu")
mole_image = pygame.image.load('mole.png')
background_image = pygame.image.load('background.png')


def draw_score():
    font = pygame.font.SysFont(None, 36)  # You can choose another font and size
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))  # White color for the score
    screen.blit(score_text, (10, 10))  # Position the score at the top-left corner


# You may need to scale the images to fit your screen size
mole_image = pygame.transform.scale(mole_image, (50, 50))  # Adjust the size as needed
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
mole_position = [random.randint(0, screen_width - 50), random.randint(0, screen_height - 50)]
score = 0

running = True
clock = pygame.time.Clock()
last_mole_move = pygame.time.get_ticks()

# event loop
while running:
    screen.blit(background_image, (0, 0))
    screen.blit(mole_image, mole_position)
    draw_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mole_image.get_rect(topleft=mole_position).collidepoint(event.pos):
                score += 1
                mole_position = [random.randint(0, screen_width - 50), random.randint(0, screen_height - 50)]
                last_mole_move = pygame.time.get_ticks()

    # Move the mole at regular intervals
    current_time = pygame.time.get_ticks()
    if current_time - last_mole_move > mole_move_interval:
        mole_position = [random.randint(0, screen_width - 50), random.randint(0, screen_height - 50)]
        last_mole_move = current_time

    pygame.display.update()
    clock.tick(60)

pygame.quit()
