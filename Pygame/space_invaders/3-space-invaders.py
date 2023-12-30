import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
ENEMY_WIDTH = 30
ENEMY_HEIGHT = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(WHITE)
player_rect = player_img.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.bottom = SCREEN_HEIGHT - 20

# Enemies
enemies = []
enemy_img = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))  # Define enemy_img
enemy_img.fill(WHITE)
for _ in range(5):
    enemy = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
    enemy.fill(WHITE)
    enemy_rect = enemy.get_rect()
    enemy_rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
    enemy_rect.y = random.randint(0, SCREEN_HEIGHT // 2)
    enemies.append(enemy_rect)

# Bullets
bullets = []
bullet_speed = 5
bullet_img = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
bullet_img.fill(WHITE)


clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.Font(None, 36)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        bullet.fill(WHITE)
        bullet_rect = bullet.get_rect()
        bullet_rect.centerx = player_rect.centerx
        bullet_rect.centery = player_rect.top
        bullets.append(bullet_rect)

    # Move bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Check for collisions
    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10

    # Draw everything
    screen.fill(BLACK)
    screen.blit(player_img, player_rect)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    for bullet in bullets:
        screen.blit(bullet_img, bullet)

    # Display the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)


# Quit the game
pygame.quit()
