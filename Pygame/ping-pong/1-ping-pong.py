import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 480
BORDER = 10
WHITE = (255, 255, 255) # beyazin rgb degeri
BLACK = (0, 0, 0) # siyahin rgb degeri

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball properties
ball_size = 15
ball_speed = [4, 4]
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

# Paddle properties
paddle_width, paddle_height = 20, 150
paddle_speed = 2
left_paddle = pygame.Rect(BORDER, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(
    WIDTH - paddle_width - BORDER,
    HEIGHT // 2 - paddle_height // 2,
    paddle_width,
    paddle_height
)

# Score
font = pygame.font.Font(None, 72)
left_score = 0
right_score = 0


def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    screen.blit(right_score_text, (3 * WIDTH // 4 - right_score_text.get_width() // 2, 20))

    pygame.display.flip()


def move_paddle(paddle, direction):
    if direction == "up" and paddle.top > BORDER:
        paddle.y -= paddle_speed
    if direction == "down" and paddle.bottom < HEIGHT - BORDER:
        paddle.y += paddle_speed


def move_ball():
    global left_score, right_score

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= BORDER or ball.bottom >= HEIGHT - BORDER:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] = -ball_speed[0]

    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()


def reset_ball():
    ball.x = WIDTH // 2 - ball_size // 2
    ball.y = HEIGHT // 2 - ball_size // 2
    ball_speed[0] = -ball_speed[0]


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_paddle(left_paddle, "up")
    if keys[pygame.K_s]:
        move_paddle(left_paddle, "down")
    if keys[pygame.K_UP]:
        move_paddle(right_paddle, "up")
    if keys[pygame.K_DOWN]:
        move_paddle(right_paddle, "down")

    move_ball()
    draw()
    time.sleep(0.01)

pygame.quit()
