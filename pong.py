import pygame

# Initialize the game
pygame.init()

# Set the width and height of the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('pong_icon.png')
pygame.display.set_icon(icon)

# Paddle A
paddle_a = pygame.Rect(30, 250, 10, 100)

# Paddle B
paddle_b = pygame.Rect(760, 250, 10, 100)

# Ball
ball = pygame.Rect(395, 295, 10, 10)
ball_speed_x = 7
ball_speed_y = 7

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= 10
    if keys[pygame.K_s] and paddle_a.bottom < 600:
        paddle_a.y += 10
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= 10
    if keys[pygame.K_DOWN] and paddle_b.bottom < 600:
        paddle_b.y += 10

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Reset ball if it goes out of bounds
    if ball.left <= 0 or ball.right >= 800:
        ball.x = 395
        ball.y = 295

    # Fill the background
    screen.fill((0, 0, 0))
    # Draw paddles and ball
    pygame.draw.rect(screen, (255, 255, 255), paddle_a)
    pygame.draw.rect(screen, (255, 255, 255), paddle_b)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    # Refresh the game screen
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()